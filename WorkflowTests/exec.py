import utils, TL
from datetime import datetime, timedelta

# API delay set to 3 secs
# epoch from, epoch to, number of connections to be created
for epoch in utils.randomize_epoch(1711909800000, 1730399400000, 10):
    TL.NewTL_mod("createdTime", epoch)

# for epoch in utils.randomize_epoch(1711909800000, 1730399400000, 10):
#     print(datetime.fromtimestamp(epoch / 1000))