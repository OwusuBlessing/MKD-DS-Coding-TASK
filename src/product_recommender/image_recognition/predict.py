import torch
from src.product_recommender.image_recognition.model import TinyVGG
from torchvision import transform
from PIL import Image

def load_tinyvgg_model(model_save_path, input_shape, hidden_units, output_shape, device):
    """
    Loads a TinyVGG model from a specified path and sends it to a specified device.

    Args:
    model_save_path (str): Path to the saved model file (.pth).
    input_shape (int): Number of input channels.
    hidden_units (int): Number of hidden units in the convolutional layers.
    output_shape (int): Number of output units (classes).
    device (str): The device to load the model onto ('cpu' or 'cuda').

    Returns:
    torch.nn.Module: Loaded PyTorch model ready for inference or further training.
    """
    # Initialize the model
    model_load = TinyVGG(input_shape=input_shape, hidden_units=hidden_units, output_shape=output_shape)

    # Load the model's saved state dictionary
    model_load.load_state_dict(torch.load(model_save_path))
    # Send the model to the specified device
    loaded_model = model_load.to(device)

    return loaded_model


#Write transform  for eaxh image
data_transform = transforms.Compose([
    #resize image
    transforms.Resize(size=(64,64)),
    #Flip image horizontally
    transforms.RandomHorizontalFlip(p=0.5),

    #Turn image to torch tensor
    transforms.ToTensor()]
)


loaded_model = load_tinyvgg_model(input_shape=3,
                                  model_save_path="/kaggle/working/models/tinyvgg_model_1.pth",
                                  hidden_units=10,
                                  output_shape=3,
                                  device =device
)



def predict(model: torch.nn.Module, 
                        image_path: str, 
                        transform=None,
                        device: torch.device = "cpu"):
    """Makes a prediction on a target image and plots the image with its prediction."""
    
    # 1. Load in image and convert the tensor values to float32
    target_image = Image.open(image_path)
    
    # 2. Divide the image pixel values by 255 to get them between [0, 1]
    #target_image = target_image / 255. 
    
    # 3. Transform if necessary
    if transform:
        target_image = transform(target_image)
    
    # 4. Make sure the model is on the target device
    model.to(device)
    
    # 5. Turn on model evaluation mode and inference mode
    model.eval()
    with torch.inference_mode():
        # Add an extra dimension to the image
        target_image = target_image.unsqueeze(dim=0)
    
        # Make a prediction on image with an extra dimension and send it to the target device
        target_image_pred = model(target_image.to(device))
        
    # 6. Convert logits -> prediction probabilities (using torch.softmax() for multi-class classification)
    target_image_pred_probs = torch.softmax(target_image_pred, dim=1)

    # 7. Convert prediction probabilities -> prediction labels
    target_image_pred_label = torch.argmax(target_image_pred_probs, dim=1)

    class_dict = {'JUMBO BAG RED RETROSPOT': 0,
 'REGENCY CAKESTAND 3 TIER': 1,
 'WHITE HANGING HEART T-LIGHT HOLDER': 2}
    
    for key, val in class_dict.items():
        if val == target_image_pred_label:
            class_name = key
            
    return class_name ,target_image_pred_label
