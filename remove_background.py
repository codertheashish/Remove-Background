from withoutbg import WithoutBG

clcoding = WithoutBG.opensource()
result = clcoding.remove_background("ashish.jpeg")
result.save("output_ashish.png")
