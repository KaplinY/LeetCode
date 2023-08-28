height = [0,1,0,2,1,0,1,3,2,1,2,1]
i=0
result = 0
while i < len(height) - 1:
    left = height[i]
    right = height[i+1]
    good_heights = []
    if right < left:
        good_heights.append(left)
        while right < left:
            i+=1
            if i == len(height):
                break
            right = height[i]
            good_heights.append(right)
    else:
        i+=1
    if good_heights:
        print(good_heights)
        l = good_heights[0]
        r = good_heights[-1]
        
        for j in range(1,len(good_heights)-1):
            water = 0
            # if good_heights[j] < l and good_heights[j] < r:
            #     water1 = min(r,l) - good_heights[j]
            x=j+1
            top = good_heights[x]
            while x < len(good_heights)-1:
                x+=1
                if good_heights[x] > top:
                    top = good_heights[x]
            if top > good_heights[j]:
                water = min(l,top) - good_heights[j] 
                print(water)               
            result+=water
print(result)

            

                

