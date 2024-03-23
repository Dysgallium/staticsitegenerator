class HTMLNode:
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __repr__(self):
        result = "HTMLNode object: "
        result += f"tag->{self.tag}, "
        result += f"value->{self.value}, "
        if self.children:
            result += "children->["
            for item in result:
                result += f"{item}, "
            result += "], "
        else:
            result += "children->[None], "
        if self.props.keys():
            result += "props->["
            for key in self.props.keys():
                result += f"{key}->{self.value[key]}, "
            result += "]"
        else:
            result += "props->[None]"
        return result
    
    def __eq__(self, other):
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for key in self.props.keys():
            result += f" {key}=\"{self.props[key]}\""
        return result
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value == None:
            raise ValueError("No value assigned")
        if not self.tag:
            return self.value
        if self.tag in ["h1", "h2", "h3", "p", "b", "i", "blockquote", "code", "li"]:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        if self.tag == "a":
            props = self.props_to_html()
            return f"<a{props}>{self.value}</a>"
        if self.tag == "img":
            props = self.props_to_html()
            return f"<img{props}>"