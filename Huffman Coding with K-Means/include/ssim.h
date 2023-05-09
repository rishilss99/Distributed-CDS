#ifndef __SSIM_H__
#define __SSIM_H__

#include <base.h>

namespace gil = boost::gil;
class SSIM: public Base
{
public:
    SSIM(const std::string &, const std::string &);
    double calculateScore();
};

#endif