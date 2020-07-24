import cv2
filepath = input("Enter your filepath: ")

cap = cv2.VideoCapture(filepath)

_, frame1 = cap.read()
while cap.isOpened():
	_, frame2 = cap.read()

	sift = cv2.SIFT()
	kp1 = sift.detectAndCompute(frame1, None)
	kp2 = sift.detectAndCompute(frame2, None)

	FLANN_INDEX_KDTREE = 0
	idx_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	searc_params = dict(checks =50)

	flann = cv2.FlannBasedMatcher(idx_params, search_params)
	matches = flann.knnMatch(des1, des2, k=2)

	good= []
	for m, n in matches:
		if m.distance<0.7*n.distance:
			good.append(n)

	src_pts = np.float32([kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
	dst_pts = np.float32([kp1[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
	M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
	matches_mask = mask.ravel().tolist()

	h, w = frame1.shape
	pts = np.float32([[0,0], [w-1, 0], [w-1, h-1], [h-1, 0]]).reshape(-1, 1, 2)
	dst = cv2.perspectiveTransform(pts,M)
	frame2 = cv2.polylines(frame2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

    #so far gives us the matching features, but I am still working on how to use that to detect football.


	frame1 = cap.read()
	k = cv2.waitKey(1) and 0xFF
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()