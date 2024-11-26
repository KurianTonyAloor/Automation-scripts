import json

def json_to_xml(json_obj, line_padding=""):
    result_list = []
    json_obj_type = type(json_obj)

    if json_obj_type is list:
        for sub_elem in json_obj:
            result_list.append(json_to_xml(sub_elem, line_padding))
        return "\n".join(result_list)

    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result_list.append(f"{line_padding}<{tag_name}>")
            result_list.append(json_to_xml(sub_obj, line_padding + "    "))
            result_list.append(f"{line_padding}</{tag_name}>")
        return "\n".join(result_list)

    return f"{line_padding}{json_obj}"

with open('input.json', 'r') as file:
    json_data = json.load(file)

xml_data = json_to_xml(json_data)

with open('output.xml', 'w') as file:
    file.write(f"<root>\n{xml_data}\n</root>")
