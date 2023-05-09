// #include <boost/filesystem.hpp>
// #include <iostream>
// #include <ssim.h>

// int main(int argc, char *argv[])
// {
//     std::string path1;
//     std::string path2;
//     std::cin >> path1 >> path2;
//     SSIM s(path1, path2);
//     std::cout << s.imagesDimensionEqual() << "\n";
// }

#include <cmath>

#include "Utility.hpp"
#include "Decoder.hpp"

void printHelp()
{
    std::cout << "===========================================" << std::endl;
    std::cout << "   K-PEG - Simple JPEG Encoder & Decoder" << std::endl;
    std::cout << "===========================================" << std::endl;
    std::cout << "Help\n"
              << std::endl;
    std::cout << "<filename.jpg>                  : Decompress a JPEG image to a PPM image" << std::endl;
    std::cout << "-h                              : Print this help message and exit" << std::endl;
}

void decodeJPEG(const std::string &filename)
{
    if (!kpeg::utils::isValidFilename(filename))
    {
        std::cout << "Invalid input file name passed." << std::endl;
        return;
    }

    std::cout << "Decoding..." << std::endl;

    kpeg::Decoder decoder;

    decoder.open(filename);
    if (decoder.decodeImageFile() == kpeg::Decoder::ResultCode::DECODE_DONE)
    {
        decoder.dumpRawData();
    }

    decoder.close();

    std::cout << "Generated file: " << filename.substr(0, filename.length() - 3) << ".ppm" << std::endl;
    std::cout << "Complete! Check log file \'kpeg.log\' for details." << std::endl;
}

int handleInput(const std::string &path)
{
    if (!path.empty())
    {
        decodeJPEG(path);
        return EXIT_SUCCESS;
    }
}

int main()
{
    try
    {
        std::string path;
        std::cin >> path;
        return handleInput(path);
    }
    catch (std::exception &e)
    {
        std::cout << "Exceptions Occurred:-" << std::endl;
        std::cout << "What: " << e.what() << std::endl;
    }

    return EXIT_SUCCESS;
}