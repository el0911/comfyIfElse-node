class AnyType(str):
  """A special class that is always equal in not equal comparisons. Credit to pythongosssss"""

  def __ne__(self, __value: object) -> bool:
    return False


any_type = AnyType("*")

class ComfyConditional:
    """
    A example noade

    Class methods
    -------------
    INPUT_TYPES (dict): 
        Tell the main program input parameters of nodes.

    Attributes
    ----------
    RETURN_TYPES (`tuple`): 
        The type of each element in the output tulple.
    RETURN_NAMES (`tuple`):
        Optional: The name of each output in the output tulple.
    FUNCTION (`str`):
        The name of the entry-point method. For example, if `FUNCTION = "execute"` then it will run Example().execute()
    OUTPUT_NODE ([`bool`]):
        If this node is an output node that outputs a result/image from the graph. The SaveImage node is an example.
        The backend iterates on these output nodes and tries to execute all their parents if their parent graph is properly connected.
        Assumed to be False if not present.
    CATEGORY (`str`):
        The category the node should appear in the UI.
    execute(s) -> tuple || None:
        The entry point method. The name of this method must be the same as the value of property `FUNCTION`.
        For example, if `FUNCTION = "execute"` then this method's name must be `execute`, if `FUNCTION = "foo"` then it must be `foo`.
    """
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(s):
        """
            Return a dictionary which contains config for all input fields.
            Some types (string): "MODEL", "VAE", "CLIP", "CONDITIONING", "LATENT", "IMAGE", "INT", "STRING", "FLOAT".
            Input types "INT", "STRING" or "FLOAT" are special values for fields on the node.
            The type can be a list for selection.

            Returns: `dict`:
                - Key input_fields_group (`string`): Can be either required, hidden or optional. A node class must have property `required`
                - Value input_fields (`dict`): Contains input fields config:
                    * Key field_name (`string`): Name of a entry-point method's argument
                    * Value field_config (`tuple`):
                        + First value is a string indicate the type of field or a list for selection.
                        + Secound value is a config for type "INT", "STRING" or "FLOAT".
        """
        return {
            "required": {
                "pipe": ("IMAGE",),
                "condition_index": ("INT", {
                    "default": 1, 
                    "min": 1, #Minimum value
                    "max": 2, #Maximum value
                    "step": 1, #Slider's step
                    "display": "number" # Cosmetic only: display as "number" or "slider"
                }),####for now just have a fixed condition 
                # "float_field": ("FLOAT", {
                #     "default": 1.0,
                #     "min": 0.0,
                #     "max": 10.0,
                #     "step": 0.01,
                #     "round": 0.001, #The value represeting the precision to round to, will be set to the step value by default. Can be set to False to disable rounding.
                #     "display": "number"}),
                # "print_to_screen": (["enable", "disable"],),
                # "string_field": ("STRING", {
                #     "multiline": False, #True if you want the field to look like the one on the ClipTextEncode node
                #     "default": "Hello World!"
                # }),
            },
        }

    RETURN_TYPES = (any_type,any_type)
    RETURN_NAMES = ("CONDITION_1","CONDITION_2",)

    FUNCTION = "evaluate"

    #OUTPUT_NODE = False

    CATEGORY = "Conditional"

    def evaluate(self, pipe,  condition_index):
        if condition_index == 1:
            return ([],pipe)
        else:
            return (pipe,[])
         


# A dictionary that contains all nodes you want to export with their names
# NOTE: names should be globally unique
NODE_CLASS_MAPPINGS = {
    "ComfyConditional": ComfyConditional
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "ComfyConditional": "Conditional Node"
}