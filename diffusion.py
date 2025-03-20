from config import get_all_images_names, IM_SIZE, DEVICE
from PIL import Image
import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F

def load_imTensor():
    images = []
    for imname in get_all_images_names():
        imobj = Image.open(imname).resize((IM_SIZE))
        imarr = np.array(imobj)[:,:,:3]
        imarr = torch.Tensor(imarr).permute(2,0,1)
        images.append(imarr)

    return torch.stack(images)

class VAE(nn.Module):
    def __init__(self, in_ch=3, hidden=[64, 128, 256, 512]):
        super(VAE, self).__init__()
        encoder = [nn.Conv2d(in_ch, hidden[0], 5, 2, dilation=2)] + [
            nn.Conv2d(hidden[i], hidden[i+1], 5, 2, dilation=2) for i in range(len(hidden)-1)
        ]
        decoder = [
            nn.ConvTranspose2d(hidden[i], hidden[i-1], 5, 2, dilation=2) for i in range(len(hidden)-1, 0, -1)
        ] + [nn.Conv2d(hidden[0], in_ch, 5, 2, dilation=2)]
        self.encoder = nn.Sequential(*encoder)
        self.decoder = nn.Sequential(*decoder)
    
    def forward(self, x):
        h = self.encoder(x)
        y = self.decoder(h)
        return y

if __name__ == "__main__":

    batch = load_imTensor()[:64].to(DEVICE)
    # im_avg = torch.mean(batch, 0).permute(1,2,0).numpy()
    # Image.fromarray(np.array(im_avg, dtype=np.uint8)).show()
    vae = VAE().to(DEVICE)
    vae.forward(batch)
        