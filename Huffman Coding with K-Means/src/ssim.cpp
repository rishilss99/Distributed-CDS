#include <ssim.h>
#include <iostream>
#include <string>
#include <boost/gil/extension/dynamic_image/algorithm.hpp>
SSIM::SSIM(const std::string &img1_path, const std::string &img2_path) : Base(img1_path, img2_path)
{
}

double SSIM::calculateScore(){
    return 0;
}