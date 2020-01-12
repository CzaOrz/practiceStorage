### [Database](#Database)
* [事务](#事务)
* [分布式事务](#分布式事务)
* [隔离级别](#隔离级别)
* [一致性哈希](#一致性哈希)
* [缓存穿透、缓存击穿和缓存雪崩](#缓存穿透、缓存击穿和缓存雪崩)

----------

## Database

#### 事务
事务就是作为单个逻辑单元执行的一组操作，要么全成功，要么全失败。<br>
这种把多条语句作为一个整体进行操作的功能，称之为数据库事务。
* A-原子性：将所有的SQL作为原子工作单元执行，即要么全执行，要么全不执行。
* C-一致性：事务完成后，所有数据的状态需要一致。
* I-隔离性：多个事务并发执行，每个事务作出的修改必须与其他事务隔离。
* D-持久性：事务完成后，对数据库的修改应该被持久化存储。

对于单条SQL语句，数据库自动将其作为一个事务执行，这种事务被称之为```隐式事务```<br>
而当需要把多条SQL语句作为一个事务执行，则需要使用BEGIN开启一个事务，
使用COMMIT提交一个事务，这种事务被称之为显式事务。
```SQL
BEGIN;
UPDATE account SET balance=balance-100 WHERE id=1;
UPDATE account SET balance=balance+100 WHERE id=2;
COMMIT;
```
当我们希望主动让事务失败，则需要使用ROOLBACK回滚事务，即整个事务会失败：
```SQL
BEGIN;
UPDATE account SET balance=balance-100 WHERE id=1;
UPDATE account SET balance=balance+100 WHERE id=2;
ROOLBACK;
```

#### 分布式事务
单数据源的一致性依靠单机事务来保证，多数据源的一致性就要依靠分布式事务。<br>
* XA分布式事务协议
    * 包含两阶段提交（2PC）和三阶段提交（3PC）
    * 2PC
        * 在XA协议中包含着两个角色：事务的协调者和事务参与者
        * 第一阶段：作为事务的协调者首先会向所有的参与者节点发送Prepare请求<br>
        在接收到请求之后，每一个节点各自执行与事务相关的数据更新，但是不提交事务<br>
        而是向事务协调者返回完成的消息
        * 第二阶段：事务协调者接收到了所有参与者的返回正向消息，则发出commit请求。<br>
        当节点成功commit提交后，会发送确认的消息，至此，整个分布式事务完成。
    * 2PC的缺点：
        * 性能问题：虽遵循强一致性，但事务执行过程中，各节点占用这数据资源<br>
        只有当所有节点准备完毕，事务协调者才会通知提交，然后参与者才会释放资源。
        * 协调者单点故障：协调者单点挂了，基本就无法完成工作。
        * 丢失消息导致不一致：即在第二阶段，发送commit的过程中，某节点未收到消息<br>
        则会导致数据的不一致性。
    * 3PC
        * 在原基础上增加了CanCommit阶段，并引入了超时机制，一旦事务参与者迟迟没有
        接到协调者的commit请求，会自动本地commit。
    * MQ事务：
        * 利用中间件来异步完成事件的后一半更新。
    * TCC事务：
        * 即Try、Commit、Cancel。

#### 隔离级别
##### Read Uncommitted
是隔离级别最低的一种事务级别。在此隔离级别下，一个事务会读到另一个
事务更新后但未提交的数据。<br>
若另一个事务回滚，那么当前事务读到的数据就是脏数据，即Dirty Read<br>

事务A、B
* A：更新了事件但是没有commit，此时B读取到的就是更新后的数据
* B：随后A进行事务回滚，B再度就又得到不同的数据，这就是脏读
总结来说就是：<br>
在Read Uncommitted隔离级别下，一个事务可能读取到另一个事务更新但未提交的数据，这个数据有可能是脏数据

##### Read Committed
在此隔离级别下，一个事务可能会遇到不可重复读的问题。<br>
就是一个事务在两次读取数据的过程中，当有另一个事务同样修改了当前数据，
并且对事务进行了commit。那么前一个事务再次读取就会得到不同数据。

##### Repeatable Read
在此隔离级别下，一个事务可能会遇到幻读Phantom Read。<br>
幻读即，在一个事务中，第一次查询某条记录是发现没有，但是当更新
这条不存在的数据时能够成功密切再次读取同一记录是，能够查询到。<br>

当一个事务进行查询为空时，另一个事务插入了这条数据。然后第一个事务
再次查询结果仍然为空，但是更新这条数据是可以成功的，之后再查就可以出结果。

##### Serializable
Serializable是最严格的隔离级别。在此级别下所有事务按照次序一次执行。
因此脏读、不可重复读、幻读都不会出现。<br>
但是事务的执行是串联执行的，效率会降低。<br>
在mysql的InnoDB引擎，默认的隔离级别是Repeatable Read


#### 一致性哈希
场景描述：<br>
三台服务器，缓存3w张图片，平均每台缓存1w张左右。<br>
如果随机存储，那么访问某个缓存项的时候，就需要遍历所有缓存知道找到目标。
花费时长太多，失去了缓存的意义。缓存本身就是为了提供速度。<br>

* 方法一：
    * 每一张图片名称是唯一的。那么可以对所有的图片名做相同的哈希计算。
    得出的结果应该都是唯一的，然后有3台服务器，我们可以将哈希后的结果
    对3取余，那么余数一定是0-2，正好对应3台服务器。<br>
    如此，下次访问的时候，可以直接计算出图片存在那台服务器上。
    * 此方法有缺陷。当增加/减少服务器的时候，固定的取余数就会出现问题，
    即已有数据和新数据可能对应不上。
        * 问题1：当缓存服务器数量发生变化的时候，会引起缓存雪崩，即可能
        引起整体系统压力过大而崩溃。
        * 问题2：当缓存服务器数量变化时，几乎所有缓存的位置都会发生改变。
* Consistent hashing
    * 将value映射在一个32位的key值中，得到一个环形hash。
    * 对于object，通过哈希算法将其映射到环形hash上。<br>
    对于cache，或者说是redis，同样哈希映射到环形hash上。<br>
    此时，object和cache都映射到了环形hash空间中，接下来顺时针计算，
    object遇到的第一个cache就是目标cache了。
    * 那么此时无论是增加节点还是移除节点，影响的范围应该都是有限的。
    * 问题：hash倾斜
        * hash计算后，分布密集。即存在节点分布不均匀的情况，同样可能会造成缓存雪崩。
    * 解决方法：引入虚拟节点
        * 虚拟节点多于实际cache节点。object会先映射到虚拟节点，然后虚拟节点会再次计算，
        从而映射到实际的cache节点。


#### 缓存穿透、缓存击穿和缓存雪崩
* 缓存穿透
    * 查询一个根本不存在的数据，每次缓存都不会命中，且处于容错考虑，
    如果从存储层查不到数据，则不写入缓存，导致每次请求都要到存储层查询。
    此时缓存就失去了意义。
    * 方法：
        * 直接缓存None值
* 缓存击穿
    * 在高并发情况下，对一个特定的值进行查询，但是该值缓存正好过期，缓存没有命中。
    导致大量请求直接落到了存储库。
* 缓存雪崩
    * 在高并发情况下，大量缓存在同一时间过期，导致大量请求落在数据库上。
    * 方法：
        * 缓存预热：即设定过期时间和预加载时间，每次缓存获取时都会计算
        达到预加载的时间，达到了则异步更新缓存。