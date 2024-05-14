class Example:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "int_field": ("INT", {
                    "default": 0,
                    "min": 0,  # Minimum value
                    "max": 4096,  # Maximum value
                    "step": 64,  # Slider's step
                    "display": "number"  # Cosmetic only: display as "number" or "slider"
                }),
                "float_field": ("FLOAT", {
                    "default": 1.0,
                    "min": 0.0,
                    "max": 10.0,
                    "step": 0.01,
                    "round": 0.001,
                    # The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                    "display": "number"}),
                "print_to_screen": (["enable", "disable"],),
                "string_field": ("STRING", {
                    "multiline": False,  # True if you want the field to look like the one on the ClipTextEncode node
                    "default": "Hello World!"
                }),
            },
        }

    RETURN_TYPES = ("IMAGE",)
    # RETURN_NAMES = ("image_output_name",)

    FUNCTION = "test"

    OUTPUT_NODE = True

    CATEGORY = "Example/test"

    def test(self, image, string_field, int_field, float_field, print_to_screen):
        if print_to_screen == "enable":
            print(f"""Your input contains:
                string_field aka input text: {string_field}
                int_field: {int_field}
                float_field: {float_field}
            """)
        # do some processing on the image, in this example I just invert it
        image = 1.0 - image
        return (image,)

    """
        The node will always be re executed if any of the inputs change but
        this method can be used to force the node to execute again even when the inputs don't change.
        You can make this node return a number or a string. This value will be compared to the one returned the last time the node was
        executed, if it is different the node will be executed again.
        This method is used in the core repo for the LoadImage node where they return the image hash as a string, if the image hash
        changes between executions the LoadImage node is executed again.
    """
    # @classmethod
    # def IS_CHANGED(s, image, string_field, int_field, float_field, print_to_screen):
    #    return ""


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique  ע��:����Ӧ����ȫ��Ψһ��
NODE_CLASS_MAPPINGS = {
    "Example": Example  # ���ڵ�������ڵ������ӳ�䡣�����ʾ���У����ڵ�����"Example"����Example����ӳ�䡣
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "Example": "Example Node"  # �ڵ��������Ѻ�/�ɶ��Ľڵ�������ӳ�䡣�����ʾ���У����ڵ�����"Example"��ڵ����"Example Node"����ӳ�䡣
}
