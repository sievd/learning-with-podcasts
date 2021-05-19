import base64


def base64_encoded_string_to_picture(base64_encoded_string, path, filename):
    data_URI, base64_value = base64_encoded_string.split(";base64,")
    extension = get_picture_extension(data_URI)
    base64_img_bytes = base64_value.encode("utf-8")
    with open(f"{path}/{filename}.{extension}", "wb") as f:
        decoded_base64 = base64.decodebytes(base64_img_bytes)
        f.write(decoded_base64)
        return f"{path}/{filename}.{extension}"


def get_picture_extension(data_URI):
    _, extension = data_URI.split("/")
    return extension
