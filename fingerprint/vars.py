from pathlib import Path


DB_NAME = "BI"
DB_IP = "10.5.18.101"


## Change as needed
DS_PREFIX = Path("~/datasets").expanduser()

## List of Available datasets
AVAIL_DS = {_.name for _ in DS_PREFIX.iterdir() if _.is_dir()}



# mongodb://MASK:8KHX1SySSn1dUJUC@51.79.52.188/mask_test

# DB_CON = f"mongodb://{DB_IP}/{DB_NAME}"