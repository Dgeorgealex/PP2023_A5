def build_xml_element(tag, content, **elements):
    attributes = ""
    for key, value in elements.items():
        attributes += f" {key}={value} "

    ans = f"<{tag}{attributes}>"
    ans += content
    ans += f"</{tag}"

    return ans


if __name__ == "__main__":
    print(build_xml_element("a", "Hello there", href=" http://python.org ", _class=" my-link ", id=" someid "))
