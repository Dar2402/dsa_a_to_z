import cv2
from loguru import logger

RTSP_URL = "rtsp://10.1.1.47:8080/h264.sdp"

def get_rtsp_capture(url: str):
    gst_pipeline = (
        f"rtspsrc location={url} latency=50 ! "
        "rtph264depay ! h264parse ! avdec_h264 ! videoconvert ! appsink"
    )

    logger.info("Opening RTSP stream...")
    cap = cv2.VideoCapture(gst_pipeline, cv2.CAP_GSTREAMER)

    if not cap.isOpened():
        logger.error("Failed to open RTSP stream")
        return None

    logger.success("RTSP stream opened successfully")
    return cap

def main():
    cap = get_rtsp_capture(RTSP_URL)
    if cap is None:
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            logger.warning("Frame grab failed, retrying...")
            continue
        logger.info(f"Frame: {frame.shape}")

if __name__ == "__main__":
    main()
