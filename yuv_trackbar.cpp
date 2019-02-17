#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"
#include <iostream>

using namespace cv;
//72,138

const String window_capture_name = "Video Capture";

const String window_detection_name = "Object Detection";

int low_Y = 0, low_U = 0, low_V = 0;
int high_Y = 255, high_U = 255, high_V = 255;

int Y,U,V;

static void on_Y_thresh_trackbar(int, void *)
{
    //Y = min(high_Y-1, low_Y);
    setTrackbarPos("Y", window_detection_name, Y);
}

static void on_U_thresh_trackbar(int, void *)
{
    //U = min(high_U-1, low_U);
    setTrackbarPos("U", window_detection_name, U);
}
static void on_V_thresh_trackbar(int, void *)
{
    //V = m(high_V-1, low_V);
    setTrackbarPos("V", window_detection_name, V);
}

int main(int argc, char* argv[])
{
    VideoCapture cap(argc > 1 ? atoi(argv[1]) : 0);
    
    namedWindow(window_capture_name);
    namedWindow(window_detection_name);

    createTrackbar("Y", window_detection_name, &Y, 255, on_Y_thresh_trackbar);
    createTrackbar("U", window_detection_name, &U, 255, on_U_thresh_trackbar);
    createTrackbar("V", window_detection_name, &V, 255, on_V_thresh_trackbar);
    
    Mat frame, frame_YUV, frame_threshold;
    while (true) {
        cap >> frame;
        if(frame.empty())
        {
            break;
        }

        cvtColor(frame, frame_YUV, COLOR_BGR2YUV);

        inRange(frame_YUV, Scalar(0,U-30,V-30), Scalar(255, U+30, V+30), frame_threshold);

        imshow(window_capture_name, frame);
        imshow(window_detection_name, frame_threshold);

        char key = (char) waitKey(30);
        if (key == 'q' || key == 27)
        {
            break;
        }

    }
    return 0;
}