import cv2

# Base abstract filter class
class Filter:
    def process(self, frame):
        """This method must be implemented by concrete filters"""
        raise NotImplementedError()

# Black and White filter
class BlackAndWhiteFilter(Filter):
    def process(self, frame):
        """Convert the frame to black and white"""
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# Mirror filter
class MirrorFilter(Filter):
    def process(self, frame):
        """Mirror - flip horizontally the frame"""
        return cv2.flip(frame, 1)

# Resize filter
class ResizeFilter(Filter):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def process(self, frame):
        """Resize the frame"""
        return cv2.resize(frame, (self.width, self.height))

# Blur filter
class BlurFilter(Filter):
    def __init__(self, ksize=(15, 15)):
        self.ksize = ksize

    def process(self, frame):
        """Apply a Gaussian blur to the frame"""
        return cv2.GaussianBlur(frame, self.ksize, 0)

# Pipeline class that chains filters together
class Pipeline:
    def __init__(self):
        self.filters = []

    def add_filter(self, filter):
        """Add a filter to the pipeline"""
        self.filters.append(filter)

    def process(self, frame):
        """Pass the frame through all filters in the pipeline"""
        for filter in self.filters:
            frame = filter.process(frame)
        return frame

def process_video(video_source=0):
    # Open the video stream
    video = cv2.VideoCapture(video_source)

    if not video.isOpened():
        print("Error: Problem with opening video stream")
        exit()

    # Create a pipeline and add filters (Black and white, mirror, resize, blur)
    pipeline = Pipeline()
    pipeline.add_filter(BlackAndWhiteFilter())
    pipeline.add_filter(MirrorFilter())
    pipeline.add_filter(ResizeFilter(320, 240))
    pipeline.add_filter(BlurFilter((15, 15)))

    while True:
    
        # Capture frame-by-frame
        ret, frame = video.read()
        if not ret:
            break

        processed_frame = pipeline.process(frame)

        # Display the processed frame
        cv2.imshow('Processed Video Stream', processed_frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    # Release video capture and close windows
    video.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    process_video('IMG_7030.mp4')
