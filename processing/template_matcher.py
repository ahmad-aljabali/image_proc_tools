import numpy as np
import cv2

def template_matcher(image,template_path, confidence_thresh=0, steps=5):
    template = cv2.imread(template_path)
    template = cv2.resize(template, (0,0), fx = 0.2, fy=0.2)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    template = cv2.Canny(template, 50, 200)
    cv2.imshow('template', template)
    (tH, tW) = template.shape[:2]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    found = None
    result = None

    # loop over multiple scales of the image
    for scale in np.linspace(0.2, 1.0, steps)[::-1]:
        resized = cv2.resize(gray, (0,0), fx = scale, fy=scale)
        r = 1/scale

        # break if the resized image is smaller than the template
        if resized.shape[0] < tH or resized.shape[1] < tW:
            break
        edged = cv2.Canny(resized, 50, 200)
        matches = cv2.matchTemplate(edged, template, method=cv2.TM_CCOEFF_NORMED)
        (_, confidence, _, maxLoc) = cv2.minMaxLoc(matches)


        # save the best fit match
        if found is None or confidence > found[0]:
            found = (confidence, maxLoc, r)

    # calculate the bounding box based on the scale ratio
    (confidence, maxLoc, r) = found
    (resultX, resultY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
    (resultW, resultH) = (int(tW * r), int(tH * r))


    if confidence >= confidence_thresh:
        result = [resultX, resultY, resultW, resultH, confidence]
    return result
