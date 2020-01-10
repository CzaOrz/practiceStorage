import os

md_directory = "./md_file"
aim_files_prefix = "interview"
feature_to_split = "----------"
save_file_name = "interview_note.md"

if __name__ == '__main__':
    from minitools import to_path

    article_directories = []
    article_content = []

    for md_file in filter(lambda x: x.startswith(aim_files_prefix) and x.endswith(".md"), os.listdir(md_directory)):
        with open(to_path(md_directory, md_file), 'r', encoding='utf-8') as r_f:
            directories, content = r_f.read().split(feature_to_split, maxsplit=1)
            article_directories.append(directories)
            article_content.append(content)
    new = "".join(article_directories + article_content)
    with open(save_file_name, 'w') as w_f:
        w_f.write(new)
