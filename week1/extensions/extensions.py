str_input = input("File name:").strip().lower()

mime_types={
    ".gif":"image/gif",
    ".jpg":"image/jpeg",
    ".jpeg":"image/jpeg",
    ".png":"image/png",
    ".pdf":"application/pdf",
    ".txt":"text/plain",
    ".zip":"application/zip"
}

type_name = ""
for type in mime_types:
    if str_input.endswith(type):
        type_name = type
        break
print(mime_types.get(type_name,"application/octet-stream"))