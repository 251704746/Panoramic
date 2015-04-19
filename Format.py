import Image
import math
import os

#��ԴͼƬ,�����Ϊ1:2��׼��ʽ
for root, dirs, files in os.walk("./SrcImg/"):
    for filename in files:     
        SrcImg = Image.open("./SrcImg/"+filename)
        xS,yS = SrcImg.size
        TraImg = Image.new('RGBA',(xS,xS/2))
        xT,yT = TraImg.size
        TraImg.paste(SrcImg,(0,(yT-yS)/2,xS,(yT-yS)/2 + yS))
        TraImg = TraImg.resize((4096,2048))
        TraImg.save("./TraImg/"+filename)
