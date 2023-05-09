#include <base.h>
#include <boost/filesystem.hpp>
#include <iostream>
#include <fstream>
#include <boost/gil/extension/io/jpeg_io.hpp>

Base::Base(const std::string &img1_path, const std::string &img2_path)
{

    if (!boost::filesystem::exists(img1_path))
    {
        std::cout << "Image 1 path is invalid."
                  << "\n";
        exit(1);
    }
    if (!boost::filesystem::exists(img2_path))
    {
        std::cout << "Image 2 path is invalid."
                  << "\n";
        exit(1);
    }
    readImage(img1_path, img2_path);
}

void Base::readImage(const std::string &img1_path, const std::string &img2_path)
{
    gil::jpeg_read_image(img1_path, img1);
    gil::jpeg_read_image(img2_path, img2);
}

bool Base::imagesDimensionEqual()
{
    return (img1.width() == img2.width() && img1.height() == img2.height());
}