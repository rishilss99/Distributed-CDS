#ifndef __BASE_H__
#define __BASE_H___

#include <string>
#include <boost/gil/gil_all.hpp>

namespace gil = boost::gil;

class Base
{
public:
    Base(const std::string &, const std::string &);
    bool imagesDimensionEqual();
    virtual double calculateScore() = 0;

protected:
    gil::rgb8_image_t img1;
    gil::rgb8_image_t img2;

private:
    void readImage(const std::string &, const std::string &);
};

#endif