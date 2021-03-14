from viapi.fileutils import FileUtils

file_utils = FileUtils("AccessKey ID", "AccessKey Secret")
oss_url = file_utils.get_oss_url("C:/111.jpg", "jpg", True)
print(oss_url)
