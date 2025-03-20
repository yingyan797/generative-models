import os, torch, dotenv

IM_SIZE = (750, 550)
DEVICE = torch.device("cuda")

def get_all_images_names():
    main_path = dotenv.get_key(".env", "main_path")
    images = []
    ftypes = ["png", "jpg", "jpeg", "pjpeg", "webp"]
    def read_images(base_dn):
        for imname in os.listdir(base_dn):
            dn = base_dn+"/"+imname
            if os.path.isfile(dn):
                images.append(dn)
                # ftypes.add(dn.split(".")[-1])
            elif os.path.isdir(dn):
                read_images(dn)
    
    read_images(main_path)
    return [fn for fn in images if fn.split(".")[-1] in ftypes]

