#
# spec file for package ffmpeg-4
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


# Create proper conflicts to make sure we require all from one version
# p:   Conflict string, eg if you need them all for requires instead
#      Default value Conflicts:
# c:   copmare string ie "<" or ">=", must be defined
# v:   version string ie. "< 42.3.4" or ">= 15.0.2.1", must be defined
%define devel_conflicts(p:c:v:) \
%define preamble_string %{-p:%{-p*}}%{!-p:Conflicts:} \
%define comparator %{-c:%{-c*}}%{!-c:%{error:Comparator not defined}} \
%define conflicts_version %{-v:%{-v*}}%{!-v:%{error:Version not defined}} \
\
%preamble_string libavcodec-devel %comparator %conflicts_version \
%preamble_string libavdevice-devel %comparator %conflicts_version \
%preamble_string libavfilter-devel %comparator %conflicts_version \
%preamble_string libavformat-devel %comparator %conflicts_version \
%preamble_string libavresample-devel %comparator %conflicts_version \
%preamble_string libavutil-devel %comparator %conflicts_version \
%preamble_string libpostproc-devel %comparator %conflicts_version \
%preamble_string libswresample-devel %comparator %conflicts_version \
%preamble_string libswscale-devel %comparator %conflicts_version \
%preamble_string ffmpeg-private-devel %comparator %conflicts_version \
%nil

# nvcodec headers only present after leap15
%bcond_with nvcodec
%if 0%{?suse_version} >= 1500
%bcond_without nvcodec
%endif
%if 0%{?BUILD_ORIG}
%bcond_with    amrwb
%bcond_without cuda_sdk
%else
%bcond_with    cuda_sdk
%endif
%bcond_with    fdk_aac_dlopen
%bcond_with    librtmp
%bcond_with    opencore
%bcond_with    smbclient
%bcond_with    x264
%bcond_with    x265
%bcond_with    xvid

%if 0%{?suse_version} > 1600
%bcond_without libaom
%bcond_without mysofa
%bcond_without vidstab
%bcond_without srt
%bcond_without codec2
%bcond_without lv2
%bcond_without librav1e
%bcond_without rubberband
%bcond_without soxr
%bcond_without zmq
%bcond_without vulkan
%bcond_without amrwb
%bcond_without opencore
%bcond_without xvid
%else
%if 0%{?suse_version} > 1500
%bcond_without mysofa
%bcond_without vidstab
%bcond_without codec2
%bcond_without rubberband
%bcond_without vulkan
%bcond_without amrwb
%bcond_without opencore
%else
%bcond_with libaom
%bcond_with mysofa
%bcond_with vidstab
%bcond_with srt
%bcond_with codec2
%bcond_with lv2
%bcond_with librav1e
%bcond_with rubberband
%bcond_with soxr
%bcond_with zmq
%bcond_with vulkan
%endif
%endif

%if 0%{?suse_version} >= 1500
%bcond_without zimg
%bcond_without openmpt
%else
%bcond_with zimg
%bcond_with openmpt
%endif

%define _name ffmpeg
%define _major_version 4
%define _major_expected 5
Name:           ffmpeg-4
Version:        4.4.8
Release:        0
Summary:        Set of libraries for working with various multimedia formats
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Video/Editors and Convertors
URL:            https://ffmpeg.org/

#Freshcode-URL: http://freshcode.club/projects/ffmpeg
#Git-Clone:     git://source.ffmpeg.org/ffmpeg
Source:         https://www.ffmpeg.org/releases/%_name-%version.tar.xz
Source2:        https://www.ffmpeg.org/releases/%_name-%version.tar.xz.asc
Source3:        ffmpeg-4-rpmlintrc
Source4:        enable_decoders
Source5:        enable_encoders
Source98:       http://ffmpeg.org/ffmpeg-devel.asc#/ffmpeg-4.keyring
Source99:       baselibs.conf
Patch1:         ffmpeg-arm6l.diff
Patch2:         ffmpeg-new-coder-errors.diff
Patch3:         ffmpeg-codec-choice.diff
Patch4:         ffmpeg-4.2-dlopen-fdk_aac.patch
Patch5:         soversion.patch
Patch9:         ffmpeg-4.4-CVE-2020-22046.patch
Patch10:        ffmpeg-chromium.patch
Patch11:        ffmpeg-libglslang-detection.patch
Patch14:        ffmpeg-glslang-cxx17.patch
Patch15:        0001-avutil-hwcontext-Don-t-assume-frames_uninit-is-reent.patch
Patch16:        0001-avcodec-libsvtav1-unbreak-build-with-latest-svtav1.patch
Patch22:        ffmpeg-c99.patch
Patch25:        ffmpeg-4-CVE-2024-12361.patch
Patch28:        ffmpeg-4-CVE-2025-25473.patch
Patch30:        ffmpeg-avcodec-libdav1d-don-t-repeatedly-parse-the-same-seq.patch
Patch32:        ffmpeg-4-CVE-2025-7700.patch
Patch33:        glslang16.patch
Patch35:        ffmpeg-4-CVE-2023-6601-shim01-6b1f68cc.patch
Patch36:        ffmpeg-4-CVE-2023-6601-shim02-954d16fa.patch
Patch37:        ffmpeg-4-CVE-2023-6601-shim03-a0cb5722.patch
Patch38:        ffmpeg-4-CVE-2023-6601-shim04-5b630743.patch
Patch39:        ffmpeg-4-CVE-2023-6601.patch
Patch40:        ffmpeg-4-CVE-2025-63757.patch
Patch41:        ffmpeg-4-CVE-2026-40962.patch
Patch42:        ffmpeg-4-CVE-2025-10256.patch
Patch43:        pcmbluray-bigendian.patch
Patch44:        ffmpeg-4-CVE-2026-64835.patch
Patch45:        ffmpeg-4-CVE-2026-64832.patch
Patch46:        ffmpeg-4-CVE-2026-64830.patch
Patch47:        ffmpeg-4-CVE-2026-66038.patch
Patch48:        ffmpeg-4-CVE-2026-66039.patch
Patch49:        ffmpeg-4-CVE-2026-58049.patch
Patch50:        ffmpeg-4-CVE-2026-64833.patch
Patch51:        ffmpeg-4-CVE-2026-64834.patch
Patch52:        ffmpeg-4-CVE-2026-65703.patch
Patch53:        ffmpeg-4-CVE-2026-65704.patch
Patch54:        ffmpeg-4-CVE-2026-65705.patch
Patch55:        ffmpeg-4-CVE-2026-65706.patch
Patch56:        ffmpeg-4-CVE-2026-66036-shim01.patch
Patch57:        ffmpeg-4-CVE-2026-66036.patch
Patch58:        ffmpeg-4-CVE-2026-70628.patch
Patch59:        ffmpeg-4-CVE-2026-70629.patch
Patch60:        ffmpeg-4-CVE-2026-70630.patch
Patch61:        ffmpeg-4-CVE-2026-70631.patch
Patch62:        ffmpeg-4-CVE-2026-70632.patch
Patch63:        ffmpeg-4-CVE-2026-75141.patch
Patch64:        ffmpeg-4-CVE-2026-75142.patch
Patch65:        ffmpeg-4-CVE-2026-75143.patch
Patch66:        ffmpeg-4-CVE-2026-75144.patch
Patch67:        ffmpeg-4-CVE-2026-75146.patch
Patch68:        ffmpeg-4-CVE-2026-38345.patch
Patch69:        ffmpeg-4-CVE-2026-38350-part01-aca41d3.patch
Patch70:        ffmpeg-4-CVE-2026-38350-part02-c44d237.patch
BuildRequires:  ladspa-devel
BuildRequires:  libgsm-devel
BuildRequires:  libmp3lame-devel
%if %{with mysofa}
BuildRequires:  libmysofa-devel
%endif
BuildRequires:  nasm
BuildRequires:  pkg-config
%ifarch x86_64
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(SvtAv1Enc) >= 0.8.4
%endif
%endif
BuildRequires:  pkgconfig(alsa)
%if %{with libaom}
BuildRequires:  pkgconfig(aom)
%endif
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(celt) >= 0.11.0
%if %{with codec2}
BuildRequires:  pkgconfig(codec2)
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
BuildRequires:  pkgconfig(dav1d)
%endif
BuildRequires:  pkgconfig(enca)
BuildRequires:  pkgconfig(fontconfig) >= 2.4.2
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi) >= 0.19.0
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libcdio_paranoia)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
%if %{with openmpt}
BuildRequires:  pkgconfig(libopenmpt)
%endif
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libraw1394)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(libxml-2.0)
%if %{with zmq}
BuildRequires:  pkgconfig(libzmq)
%endif
%if %{with lv2}
BuildRequires:  pkgconfig(lilv-0)
%endif
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(opus)
%if %{with librav1e}
BuildRequires:  pkgconfig(rav1e)
%endif
%if %{with rubberband}
BuildRequires:  pkgconfig(rubberband)
%endif
BuildRequires:  pkgconfig(sdl2)
%if %{with smbclient}
BuildRequires:  pkgconfig(smbclient)
%endif
%if %{with soxr}
BuildRequires:  pkgconfig(soxr)
%endif
BuildRequires:  pkgconfig(speex)
%if %{with srt}
BuildRequires:  pkgconfig(srt)
%endif
BuildRequires:  pkgconfig(theora) >= 1.1
BuildRequires:  pkgconfig(twolame)
BuildRequires:  pkgconfig(vdpau)
%if %{with vidstab}
BuildRequires:  pkgconfig(vidstab) >= 0.98
%endif
%if %{with vulkan}
BuildRequires:  c++_compiler
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(SPIRV-Tools)
BuildRequires:  pkgconfig(vulkan)
%endif
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
%if %{with zimg}
BuildRequires:  pkgconfig(zimg)
%endif
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(zvbi-0.2) >= 0.2.28
%if %{with fdk_aac_dlopen}
BuildRequires:  pkgconfig(fdk-aac)
%endif
%if %{with librtmp}
BuildRequires:  pkgconfig(librtmp)
%endif
%if %{with nvcodec}
BuildRequires:  pkgconfig(ffnvcodec)
%endif
%if %{with xvid}
BuildRequires:  libxvidcore-devel
%endif
%if %{with opencore}
BuildRequires:  pkgconfig(opencore-amrnb)
%endif
%if %{with amrwb}
BuildRequires:  pkgconfig(vo-amrwbenc)
%endif
%if %{with x264}
BuildRequires:  pkgconfig(x264)
%endif
%if %{with x265}
BuildRequires:  pkgconfig(x265)
%endif
Provides:       ffmpeg-tools = %version
Conflicts:      ffmpeg-tools
Provides:       ffmpeg = %version
Obsoletes:      ffmpeg < %version
Requires:       libavcodec58_134 = %version-%release
Requires:       libavdevice58_13 = %version-%release
Requires:       libavfilter7_110 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavresample4_0 = %version-%release
Requires:       libavutil56_70 = %version-%release
Requires:       libpostproc55_9 = %version-%release
Requires:       libswresample3_9 = %version-%release
Requires:       libswscale5_9 = %version-%release

%description
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package -n libavcodec58_134
Summary:        FFmpeg codec library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release
Requires:       libswresample3_9 = %version-%release
%if 0%{?BUILD_ORIG}
Provides:       libavcodec-full = %version-%release
# This can be (and is) required by packages like vlc-codecs -
# do follow the shlib name to not get random lib providers
Provides:       libavcodec58_134(unrestricted)
%endif
# For mozillas
Provides:       libavcodec = %version-%release

%description -n libavcodec58_134
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavcodec-devel
Summary:        Development files for FFmpeg's codec library
Group:          Development/Libraries/C and C++
Provides:       libavcodec-devel = %version-%release
Obsoletes:      libavcodec-devel < %version-%release
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavcodec58_134 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavcodec-devel
The libavcodec library provides a generic encoding/decoding framework
and contains multiple decoders and encoders for audio, video and
subtitle streams, and several bitstream filters.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavdevice58_13
Summary:        FFmpeg device library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavfilter7_110 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavutil56_70 = %version-%release

%description -n libavdevice58_13
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

%package libavdevice-devel
Summary:        Development files for FFmpeg's device library
Group:          Development/Libraries/C and C++
Provides:       ffmpeg-devel = %version-%release
Conflicts:      ffmpeg-devel
Provides:       libavdevice-devel = %version-%release
Obsoletes:      libavdevice-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavfilter-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavdevice58_13 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavdevice-devel
The libavdevice library provides a generic framework for grabbing from
and rendering to many common multimedia input/output devices, and
supports several input and output devices, including Video4Linux2, VfW,
DShow, and ALSA.

This subpackage contains the headers for FFmpeg libavcodec.

%package -n libavfilter7_110
Summary:        FFmpeg audio and video filtering library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavformat58_76 = %version-%release
Requires:       libavresample4_0 = %version-%release
Requires:       libavutil56_70 = %version-%release
Requires:       libpostproc55_9 = %version-%release
Requires:       libswresample3_9 = %version-%release
Requires:       libswscale5_9 = %version-%release

%description -n libavfilter7_110
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

%package libavfilter-devel
Summary:        Development files for FFmpeg's audio/video filter library
Group:          Development/Libraries/C and C++
Provides:       libavfilter-devel = %version-%release
Obsoletes:      libavfilter-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavresample-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libpostproc-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       %name-libswscale-devel = %version-%release
Requires:       libavfilter7_110 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavfilter-devel
The libavfilter library provides a generic audio/video filtering
framework containing several filters, sources and sinks.

This subpackage contains the headers for FFmpeg libavfilter.

%package -n libavformat58_76
Summary:        FFmpeg's stream format library
Group:          System/Libraries
Requires:       libavcodec58_134 = %version-%release
Requires:       libavutil56_70 = %version-%release

%description -n libavformat58_76
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.
%if !0%{?BUILD_ORIG}

This build of ffmpeg is limited in the number of codecs supported.
%endif

%package libavformat-devel
Summary:        Development files for FFmpeg's stream format library
Group:          Development/Libraries/C and C++
Provides:       libavformat-devel = %version-%release
Obsoletes:      libavformat-devel < %version-%release
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       %name-libswresample-devel = %version-%release
Requires:       libavformat58_76 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavformat-devel
The libavformat library provides a generic framework for multiplexing
and demultiplexing (muxing and demuxing) audio, video and subtitle
streams. It encompasses multiple muxers and demuxers for multimedia
container formats.

This subpackage contains the headers for FFmpeg libavformat.

%package -n libavresample4_0
Summary:        FFmpeg alternate audio resampling library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release
Obsoletes:      libavresample4 < %version-%release
Provides:       libavresample4 = %version-%release

%description -n libavresample4_0
An audio resampling library that is being provided for drop-in
compatibility with libav.

It is advised to use libswresample for new code.

%package libavresample-devel
Summary:        Development files for libavresample as present in FFmpeg
Group:          Development/Libraries/C and C++
Provides:       libavresample-devel = %version-%release
Obsoletes:      libavresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libavresample4_0 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavresample-devel
An audio resampling library that is being provided for drop-in
compatibility with libav.

It is advised to use libswresample for new code.

This subpackage contains the headers for FFmpeg's copy of libavresample.

%package -n libavutil56_70
Summary:        FFmpeg's utility library
Group:          System/Libraries

%description -n libavutil56_70
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

%package libavutil-devel
Summary:        Development files for FFmpeg's utility library
Group:          Development/Libraries/C and C++
Provides:       libavutil-devel = %version-%release
Obsoletes:      libavutil-devel < %version-%release
Requires:       libavutil56_70 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libavutil-devel
The libavutil library is a utility library to aid portable multimedia
programming. It contains safe portable string functions, random
number generators, data structures, additional mathematics functions,
cryptography and multimedia related functionality (like enumerations
for pixel and sample formats).

This subpackage contains the headers for FFmpeg libavutil.

%package -n libpostproc55_9
Summary:        FFmpeg post-processing library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libpostproc55_9
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

%package libpostproc-devel
Summary:        Development files for the FFmpeg post-processing library
Group:          Development/Libraries/C and C++
Provides:       libpostproc-devel = %version-%release
Obsoletes:      libpostproc-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libpostproc55_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libpostproc-devel
A library with video postprocessing filters, such as deblocking and
deringing filters, noise reduction, automatic contrast and brightness
correction, linear/cubic interpolating deinterlacing.

This subpackage contains the headers for FFmpeg libpostproc.

%package -n libswresample3_9
Summary:        FFmpeg software resampling library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libswresample3_9
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

%package libswresample-devel
Summary:        Development files for the FFmpeg software resampling library
Group:          Development/Libraries/C and C++
Provides:       libswresample-devel = %version-%release
Obsoletes:      libswresample-devel < %version-%release
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswresample3_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswresample-devel
The libswresample library performs audio conversion between different
sample rates, channel layout and channel formats.

This subpackage contains the headers for FFmpeg libswresample.

%package -n libswscale5_9
Summary:        FFmpeg image scaling and colorspace/pixel conversion library
Group:          System/Libraries
Requires:       libavutil56_70 = %version-%release

%description -n libswscale5_9
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

%package libswscale-devel
Summary:        Development files for FFmpeg's image scaling and colorspace library
Group:          Development/Libraries/C and C++
Provides:       libswscale-devel = %version-%release
Conflicts:      libswscale-devel
Requires:       %name-libavutil-devel = %version-%release
Requires:       libswscale5_9 = %version-%release
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description libswscale-devel
The libswscale library performs image scaling and colorspace and
pixel format conversion operations.

This subpackage contains the headers for FFmpeg libswscale.

%package private-devel
Summary:        Some FFmpeg private headers
Group:          Development/Libraries/C and C++
Requires:       %name-libavcodec-devel = %version-%release
Requires:       %name-libavformat-devel = %version-%release
Requires:       %name-libavutil-devel = %version-%release
Provides:       ffmpeg-private-devel = %version
Obsoletes:      ffmpeg-private-devel < %version
%devel_conflicts -c < -v %_major_version
%devel_conflicts -c >= -v %_major_expected

%description private-devel
FFmpeg is a multimedia framework, able to decode, encode,
transcode, mux, demux, stream, filter and play several formats
that humans and machines have created.

This package contains some private headers for libavformat, libavcodec and
libavutil which are needed by libav-tools to build. No other package apart
from libav should depend on these private headers which are expected to
break compatibility without any notice.

%prep
%autosetup -p1 -n %_name-%version

%build
%ifarch %ix86 %arm
%define _lto_cflags %nil
%endif
%if "%_lto_cflags" != ""
%global _lto_cflags %_lto_cflags -ffat-lto-objects
%endif
CFLAGS="%optflags" CXXFLAGS="%optflags" \
%if %suse_version > 1500
%ifarch %ix86
%else
LDFLAGS="%_lto_cflags" \
%endif
%endif
./configure \
	--prefix="%_prefix" \
	--libdir="%_libdir" \
	--shlibdir="%_libdir" \
	--incdir="%_includedir/ffmpeg" \
	--extra-cflags="%optflags" \
	--optflags="%optflags" \
	--disable-htmlpages \
	--enable-pic \
	--disable-stripping \
	--enable-shared \
	--disable-static \
	--enable-gpl \
	--enable-version3 \
%if %{with smbclient}
	--enable-libsmbclient \
%endif
	--disable-openssl \
	--enable-avresample \
	--enable-gnutls \
	--enable-ladspa \
%if %{with vulkan}
	--enable-vulkan \
	--enable-libglslang \
%endif
%if ! %{with cuda_sdk}
	--disable-cuda-sdk \
%endif
%if %{with libaom}
	--enable-libaom \
%endif
	--enable-libass \
	--enable-libbluray \
	--enable-libbs2b \
	--enable-libcelt \
	--enable-libcdio \
%if %{with codec2}
	--enable-libcodec2 \
%endif
%if 0%{?suse_version} > 1500 || 0%{?sle_version} >= 150200
	--enable-libdav1d \
%endif
	--enable-libdc1394 \
	--enable-libdrm \
	--enable-libfontconfig \
	--enable-libfreetype \
	--enable-libfribidi \
	--enable-libgsm \
	--enable-libjack \
	--enable-libmp3lame \
%if %{with mysofa}
	--enable-libmysofa \
%endif
	--enable-libopenjpeg \
%if %{with openmpt}
	--enable-libopenmpt \
%endif
	--enable-libopus \
	--enable-libpulse \
%if %{with librav1e}
	--enable-librav1e \
%endif
%if %{with rubberband}
	--enable-librubberband \
%endif
%ifarch x86_64
%if 0%{?suse_version} >= 1550
	--enable-libsvtav1 \
%endif
%endif
%if %{with soxr}
	--enable-libsoxr \
%endif
	--enable-libspeex \
	--enable-libssh \
%if %{with srt}
	--enable-libsrt \
%endif
	--enable-libtheora \
	--enable-libtwolame \
%if %{with vidstab}
	--enable-libvidstab \
%endif
	--enable-libvorbis \
	--enable-libv4l2 \
	--enable-libvpx \
	--enable-libwebp \
	--enable-libxml2 \
%if %{with zimg}
	--enable-libzimg \
%endif
%if %{with zmq}
	--enable-libzmq \
%endif
	--enable-libzvbi \
%if 0%{?suse_version} > 1500
%ifarch %ix86
%else
  --enable-lto \
%endif
%endif
%if %{with lv2}
	--enable-lv2 \
%endif
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
%endif
	--enable-vaapi \
	--enable-vdpau \
	--enable-version3 \
%if %{with fdk_aac_dlopen}
	--enable-libfdk-aac-dlopen \
	--enable-nonfree \
%endif
%if %{with opencore}
	--enable-libopencore-amrnb \
	--enable-libopencore-amrwb \
%endif
%if %{with amrwb}
	--enable-libvo-amrwbenc \
%endif
%if %{with x264}
	--enable-libx264 \
%endif
%if %{with x265}
	--enable-libx265 \
%endif
%if %{with librtmp}
	--enable-librtmp \
%endif
%if %{with xvid}
	--enable-libxvid \
%endif
%if !0%{?BUILD_ORIG}
	--enable-muxers \
	--enable-demuxers \
	--disable-encoders \
	--disable-decoders \
	--disable-decoder=h264,hevc,vc1 \
	--enable-encoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_encoders)" \
	--enable-decoder="$(perl -pe 's{^(\w*).*}{$1,}gs' <%_sourcedir/enable_decoders)" \

for i in H264 HEVC VC1; do
	grep -q "#define CONFIG_${i}_DECODER 0" config.h
done
%endif

cat config.h
%make_build

%global extratools aviocat cws2fws ffescape ffeval ffhash fourcc2pixfmt graph2dot ismindex pktdumper probetest qt-faststart seek_print sidxindex trasher

for i in %extratools; do
	%make_build "tools/$i"
done

%install
b="%buildroot"
%make_install install-man
rm -Rf "$b/%_datadir/ffmpeg/examples"
for i in %extratools; do
	cp -a "tools/$i" "$b/%_bindir/"
done

# Install private headers required by libav-tools
for i in libavformat/options_table.h libavformat/os_support.h \
  libavformat/internal.h libavcodec/options_table.h libavutil/libm.h \
  libavutil/internal.h libavutil/colorspace.h libavutil/timer.h \
  libavutil/x86/emms.h libavutil/aarch64/timer.h libavutil/arm/timer.h \
  libavutil/bfin/timer.h libavutil/ppc/timer.h libavutil/x86/timer.h; do
	mkdir -p "$b/%_includedir/ffmpeg/private/"`dirname $i`
	cp -a $i "$b/%_includedir/ffmpeg/private/$i"
done

%ldconfig_scriptlets -n libavcodec58_134
%ldconfig_scriptlets -n libavdevice58_13
%ldconfig_scriptlets -n libavfilter7_110
%ldconfig_scriptlets -n libavformat58_76
%ldconfig_scriptlets -n libavresample4_0
%ldconfig_scriptlets -n libavutil56_70
%ldconfig_scriptlets -n libpostproc55_9
%ldconfig_scriptlets -n libswresample3_9
%ldconfig_scriptlets -n libswscale5_9

%files
%doc Changelog CREDITS README.md
%_bindir/aviocat
%_bindir/cws2fws
%_bindir/ffescape
%_bindir/ffeval
%_bindir/ffhash
%_bindir/ffmpeg
%_bindir/ffplay
%_bindir/ffprobe
%_bindir/fourcc2pixfmt
%_bindir/graph2dot
%_bindir/ismindex
%_bindir/pktdumper
%_bindir/probetest
%_bindir/qt-faststart
%_bindir/seek_print
%_bindir/sidxindex
%_bindir/trasher
%_mandir/man1/ff*.1*
%_datadir/ffmpeg/
%_libdir/libavcodec.so.58
%_libdir/libavdevice.so.58
%_libdir/libavfilter.so.7
%_libdir/libavformat.so.58
%_libdir/libavresample.so.4
%_libdir/libavutil.so.56
%_libdir/libpostproc.so.55
%_libdir/libswresample.so.3
%_libdir/libswscale.so.5

%files -n libavcodec58_134
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavcodec.so.58.134*

%files -n libavdevice58_13
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavdevice.so.58.13*

%files -n libavfilter7_110
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavfilter.so.7.110*

%files -n libavformat58_76
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavformat.so.58.76*

%files -n libavresample4_0
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavresample.so.4.0*

%files -n libavutil56_70
%license COPYING.GPLv2 LICENSE.md
%_libdir/libavutil.so.56.70*

%files -n libpostproc55_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libpostproc.so.55.9*

%files -n libswresample3_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswresample.so.3.9*

%files -n libswscale5_9
%license COPYING.GPLv2 LICENSE.md
%_libdir/libswscale.so.5.9*

%files libavcodec-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavcodec/
%_libdir/libavcodec.so
%_libdir/pkgconfig/libavcodec.pc
%_mandir/man3/libavcodec.3*

%files libavdevice-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavdevice/
%_libdir/libavdevice.so
%_libdir/pkgconfig/libavdevice.pc
%_mandir/man3/libavdevice.3*

%files libavfilter-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavfilter/
%_libdir/libavfilter.so
%_libdir/pkgconfig/libavfilter.pc
%_mandir/man3/libavfilter.3*

%files libavformat-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavformat/
%_libdir/libavformat.so
%_libdir/pkgconfig/libavformat.pc
%_mandir/man3/libavformat.3*

%files libavresample-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavresample/
%_libdir/libavresample.so
%_libdir/pkgconfig/libavresample.pc

%files libavutil-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libavutil/
%_libdir/libavutil.so
%_libdir/pkgconfig/libavutil.pc
%_mandir/man3/libavutil.3*

%files libpostproc-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libpostproc/
%_libdir/libpostproc.so
%_libdir/pkgconfig/libpostproc.pc

%files libswresample-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswresample/
%_libdir/libswresample.so
%_libdir/pkgconfig/libswresample.pc
%_mandir/man3/libswresample.3*

%files libswscale-devel
%dir %_includedir/ffmpeg/
%_includedir/ffmpeg/libswscale/
%_libdir/libswscale.so
%_libdir/pkgconfig/libswscale.pc
%_mandir/man3/libswscale.3*

%files private-devel
%_includedir/ffmpeg/private/

%changelog
* Mon Sep 21 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-75141.patch:
  Backport acf5d7cd from upstream, avformat/hevc: reject hvcC
  NAL arrays that overflow the 16-bit count.
  (CVE-2026-75141, bsc#1276407)
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-38350-part02-c44d237.patch:
  Backport c44d237d from upstream, swscale/output: Fix integer
  overflow with lum/chr/alpha filter.
  (CVE-2026-38350, bsc#1277370)
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-38350-part01-aca41d3.patch:
  Backport aca41d3d from upstream, swscale/output: Fix all bilinear
  integer overflows.
  (CVE-2026-38350, bsc#1277370)
* Fri Sep 11 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-38345.patch:
  Backport 04fe9848 from upstream, libswscale/utils: prevent division
  by zero for chroma width 8.
  (CVE-2026-38345, bsc#1277376)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-75146.patch:
  Backport 65b0dab9 from upstream, avformat/dashdec: reject a negative
  fragment index.
  (CVE-2026-75146, bsc#1276412)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-75144.patch:
  Backport 1c10bcc2 from upstream, avformat/rtpenc_vc2hq: reject data
  units larger than the RTP payload buffer.
  (CVE-2026-75144, bsc#1276410)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-75143.patch:
  Backport 1c10bcc2 from upstream, avformat/librist: honor the caller
  buffer size in librist_read.
  (CVE-2026-75143, bsc#1276409)
* Fri Aug 28 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-75142.patch:
  Backport 9d786e4b from upstream, avformat/mpegenc: reject stream
  counts that overflow the system header.
  (CVE-2026-75142, bsc#1276408)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-70632.patch:
  Backport 16b2049d from upstream, avcodec/cfhd: reject transform-2
  output wider than the plane.
  (CVE-2026-70632, bsc#1274289)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-70631.patch:
  Backport 3c287af3 from upstream, avcodec/tiff: reject inflate
  output shorter than the strip.
  (CVE-2026-70631, bsc#1274287)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-70630.patch:
  Backport c22667d0 from upstream, avcodec/screenpresso: reject
  deflate output shorter than the frame.
  (CVE-2026-70630, bsc#1274282)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-70629.patch:
  Backport a5fe21a1 from upstream, avcodec/rscc: do not leave
  uninitilized data when the input is too short.
  (CVE-2026-70629, bsc#1274270)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-70628.patch:
  Backport 02fc47e1 from upstream, avcodec/dvbsub_parser: avoid
  signed overflow in the capacity check.
  (CVE-2026-70628, bsc#1274268)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-66036.patch:
  Backport 62294b6a from upstream, avfilter/vf_hqdn3d: support
  dynamic frame sizes.
  (CVE-2026-66036, bsc#1272763)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-66036-shim01.patch
  Backport e3d0c719 from upstream, avfilter/vf_hqdn3d: reject
  unsupported frame parameter changes. This patch is for facilitate
  ffmpeg-CVE-2026-66036.patch.
  (CVE-2026-66036, bsc#1272763)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-65706.patch:
  Backport b3c7ebc1 from upstream, avfilter/vf_swaprect: size the
  temp row buffer for the widest plane.
  (CVE-2026-65706, bsc#1272762)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-65705.patch:
  Backport 30a52276 from upstream, avfilter/vf_floodfill: remove
  unneeded variables.
  (CVE-2026-65705, bsc#1272761)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-65704.patch:
  Backport 52f7983f from upstream, avformat/ty: don't let the Series2
  AC3 trim underflow the packet size.
  (CVE-2026-65704, bsc#1272760)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-65703.patch:
  Backport 3b85fbe8 from upstream, avcodec/tdsc: unref the reference
  frame before reallocating on size change.
  (CVE-2026-65703, bsc#1272759)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-64834.patch:
  Backport 3c441711 from upstream, avformat/rtpdec_asf: reject ASF
  objects smaller than their header.
  (CVE-2026-64834, bsc#1272757)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-64833.patch:
  Backport 385ac2fa from upstream, avformat/spdifenc: bound DTS
  core_size against the packet size in the HD path.
  (CVE-2026-64833, bsc#1272755)
* Fri Aug 14 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2026-58049.patch:
  Backport f8d7795d from upstream, avcodec/rasc: Check that 32-bit
  DLTA accesses stay within the row.
  (CVE-2026-58049, bsc#1269550)
* Thu Jul 30 2026 Xiaoguang Wang <xiaoguang.wang@suse.com>
- Add CVE patches:
  ffmpeg-4-CVE-2026-64835.patch: (CVE-2026-64835, bsc#1272758)
  ffmpeg-4-CVE-2026-64832.patch: (CVE-2026-64832, bsc#1272754)
  ffmpeg-4-CVE-2026-64830.patch: (CVE-2026-64830, bsc#1272752)
  ffmpeg-4-CVE-2026-66038.patch: (CVE-2026-66038, bsc#1272768)
  ffmpeg-4-CVE-2026-66039.patch: (CVE-2026-66039, bsc#1272765)
* Fri Jun 26 2026 Jan Engelhardt <jengelh@inai.de>
- Add pcmbluray-bigendian.patch to address a build failure on s390x
- Update to release 4.4.8
  * Various bug fixes to codecs
  * avcodec/magicyuv: Fix 1 line MEDIAN slices
  * avcodec/magicyuv: Expand the s->interlaced slice-height sanity check
  * avcodec/magicyuv: reject slice_height misaligned with chroma vshift
    (CVE-2026-8461, bsc#1269490)
  * swscale/alphablend: don't overread alpha plane on subsampled odd size.
    (CVE-2026-38347, bsc#1277373)
  * avformat/hls: check return value of new_init_section().
    (CVE-2023-6603, bsc#1220547)
- Delete ffmpeg-4-CVE-2025-22921.patch (merged)
* Sat May 23 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2025-10256.patch:
  Backport a2546248 from upstream, Add check for the return value
  of av_malloc_array() to avoid potential NULL pointer dereference.
  (CVE-2025-10256, bsc#1249431)
* Fri May 22 2026 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.4.7:
  * Codecs, filters and other various bugfixes
  * aacenc_tns: clamp filter direction energy measurement.
    (CVE-2025-1594, bsc#1237561)
  * avcodec/jpeg2000dec: implement cdef remapping during pixel format matching.
    (CVE-2025-9951, bsc#1249393)
  * avcodec/av1dec: check that primary_ref_frame is within range.
    (CVE-2026-30997, bsc#1262047)
  * avcodec/rasc: fix heap use-after-free in decode_move().
    (CVE-2026-12706, bsc#1268595)
  * avcodec/tdsc: remove double stride adjustment.
    (CVE-2026-18393, bsc#1277377)
  * swscale/output: Fixes integer overflow in yuv2planeX_8_c.
    (CVE-2026-38346, bsc#1277375)
  * swscale/output: Fix integer overflow in alpha in yuv2rgba64_1_c_template().
    (CVE-2026-38349, bsc#1277369)
  * swscale/utils: Check *Inc.
    (CVE-2026-38348, bsc#1277368)
  * avcodec/ppc/vp8dsp_altivec: Fix out-of-bounds access.
    (CVE-2024-35367, bsc#1234029)
- Drop patches fixed upstream:
  * ffmpeg-4-CVE-2024-35368.patch
  * ffmpeg-4-CVE-2024-36618.patch
  * ffmpeg-4-CVE-2025-59728.patch
- Rebase patches with quilt.
* Wed May 13 2026 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-4-CVE-2026-40962.patch: Use 64bit in CENC subsample
  bounds checks. (CVE-2026-40962, bsc#1262237)
* Thu Jan 15 2026 SongChuan Kang <sckang@suse.com>
- Add ffmpeg-4-CVE-2025-63757.patch: Backport 0c6b7f948 from
  upstream. swscale/output: Fix integer overflow in
  yuv2ya16_X_c_template() (bsc#1255392, CVE-2025-63757).
* Thu Jan  8 2026 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2023-6601-shim01-6b1f68cc.patch:
  Backport 6b1f68cc from upstream, fail on probing non hls/m3u8 file
  extensions. Its unexpected that a .avi or other "standard" file turns
  into a playlist. The goal of this patch is to avoid this unexpected
  behavior and possible privacy or security differences.
  (CVE-2023-6601, bsc#1220545)
- Add ffmpeg-4-CVE-2023-6601-shim02-954d16fa.patch:
  Backport 954d16fa from upstream, Try to implement RFC8216 playlist
  refusal.
  (CVE-2023-6601, bsc#1220545)
- Add ffmpeg-4-CVE-2023-6601-shim03-a0cb5722.patch:
  Backport a0cb5722 from upstream, Check mime_ok first, This should
  be a few nano seconds faster (not measureable), But Collectively
  the whole humankind watching hls will safe a minute.
  (CVE-2023-6601, bsc#1220545)
- Add ffmpeg-4-CVE-2023-6601-shim04-5b630743.patch:
  Backport 5b630743 from upstream, Better message from hls_probe()
  (CVE-2023-6601, bsc#1220545)
- Add ffmpeg-4-CVE-2023-6601.patch:
  Backport d09f50c0f from upstream, remove non standard hls
  extension.
  (CVE-2023-6601, bsc#1220545)
* Wed Oct 15 2025 SongChuan Kang <sckang@suse.com>
- Add ffmpeg-4-CVE-2025-59728.patch: avformat/dashdec: Allocate
  space for appended "/" (bsc#1251137, CVE-2025-59728).
* Tue Oct  7 2025 olaf@aepfle.de
- add missing closing brace to ffmpeg-4-CVE-2025-7700.patch
* Mon Sep 29 2025 Jan Engelhardt <jengelh@inai.de>
- Add glslang16.patch to resolve FTBFS
* Wed Jul 23 2025 SongChuan Kang <sckang@suse.com>
- Add ffmpeg-4-CVE-2025-7700.patch: Add check for the return value
  of av_malloc_array() and av_calloc() to avoid potential NULL
  pointer dereference(CVE-2025-7700, bsc#1246790).
* Fri May 30 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2024-36618.patch:
  Backport 7a089ed8 from upstream, avformat/avidec: Fix integer
  overflow iff ULONG_MAX < INT64_MAX.
  (CVE-2024-36618, bsc#1234020)
* Thu May 29 2025 Jan Engelhardt <jengelh@inai.de>
- Update to release 4.4.6
  * lavc/libx265: unbreak build for X265_BUILD >= 210
  * ARM: vp9mc: Load only 12 pixels in the 4 pixel wide
    horizontal filter
  * rtmpproto: Avoid rare crashes in the `fail:` codepath in
    rtmp_open
  * avcodec/snow: Fix off by 1 error in run_buffer
  * avcodec/mpegvideo_enc: Check FLV1 resolution limits
  * avformat/hls: Be more picky on extensions.
    (CVE-2023-6602, bsc#1220546, CVE-2023-6604, bsc#1220549)
- Delete ffmpeg-CVE-2023-49502.patch,
  0001-libavcodec-arm-mlpdsp_armv5te-fix-label-format-to-wo.patch,
  ffmpeg-4-CVE-2025-0518.patch, ffmpeg-4-CVE-2025-22919.patch (merged)
* Wed Mar  5 2025 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-libsvtav1-unbreak-build-with-latest-svtav1.patch
  to build with SVT-AV1 3.0.0.
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2025-22921.patch:
  Backport 7f9c7f98 from upstream, clear array length when
  freeing it.
  (CVE-2025-22921, bsc#1237382)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2025-25473.patch:
  Backport c08d3004 from upstream, clear FFFormatContext packet.
  When packet_buffer is used in mux.c, and if a muxing process fails
  at a point where packets remained in said queue.
  (CVE-2025-25473, bsc#1237351)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2025-0518.patch:
  Backport b5b6391d from upstream, fixes memory data leak when
  use sscanf().
  (CVE-2025-0518, bsc#1236007)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2025-22919.patch:
  Backport 1446e37d from upstream, check for valid sample rate
  As the sample rate <= 0 is invalid.
  (CVE-2025-22919, bsc#1237371)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2024-12361.patch:
  Backport 4065ff69 from upstream, add check for av_packet_new_side_data()
  to avoid null pointer dereference if allocation fails.
  (CVE-2024-12361, bsc#1237358)
* Wed Feb 19 2025 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2024-35368.patch:
  Backport 45133009 from upstream, After having created the
  AVBuffer that is put into frame->buf[0], ownership of several
  objects Fix double-free on the AVFrame is unreferenced.
  (CVE-2024-35368, bsc#1234028)
* Mon Jan  6 2025 Jan Engelhardt <jengelh@inai.de>
- Update to release 4.4.5
  * Reliability/bug fixes
  Fixes: 51896/clusterfuzz-testcase-minimized-ffmpeg_dem_DXA_fuzzer-5730576523198464
  Fixes: signed integer overflow: 2147483566 + 82 cannot be represented in type 'int'
  (CVE-2024-36613, bsc#1235092)
  avformat/cafdec: dont seek beyond 64bit (CVE-2024-36617, bsc#1234019).
  avformat/westwood_vqa: Fix 2g packets (CVE-2024-36616, bsc#1234018).
  avformat/sbgdec: Check for negative duration (CVE-2024-35366, bsc#1234030).
- Delete
  0001-avcodec-libsvtav1-remove-compressed_ten_bit_format-a.patch
  0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
  0001-avfilter-vf_minterpolate-Check-pts-before-division.patch
  ffmpeg-CVE-2023-51793.patch
  0001-avfilter-af_stereowiden-Check-length.patch
  ffmpeg-fix-new-binutils.patch
  ffmpeg-CVE-2023-50010.patch
  ffmpeg-4-CVE-2024-32230.patch
  ffmpeg-4-CVE-2024-7055.patch (all merged)
  (CVE-2023-51798, bsc#1223304)
* Tue Oct 15 2024 Antonio Larrosa <alarrosa@suse.com>
- Adjust bconds to build the package in SLFO without xvidcore.
* Fri Sep  6 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2024-7055.patch:
  Backport 3faadbe2 from upstream, Use 64bit for input size check,
  Fixes: out of array read, Fixes: poc3.
  (CVE-2024-7055, bsc#1229026)
* Wed Aug 28 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-libavcodec-arm-mlpdsp_armv5te-fix-label-format-to-wo.patch
  [boo#1229338]
* Fri Jul 26 2024 Filip Kastl <filip.kastl@suse.com>
- Add ffmpeg-c99.patch so that the package conforms to the C99
  standard and builds on i586 with GCC 14.
* Tue Jul  2 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-4-CVE-2024-32230.patch:
  Backport 96449cfe from upstream, Fix 1 line and one column images.
  (CVE-2024-32230, bsc#1227296)
* Sat Apr 27 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-CVE-2023-50010.patch:
  Backport e4d2666b from upstream, fixes the out of array access.
  (CVE-2023-50010, bsc#1223256)
* Fri Apr 26 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avfilter-af_stereowiden-Check-length.patch
  [boo#1223437, CVE-2023-51794]
* Tue Apr 23 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-CVE-2023-51793.patch:
  Backport 0ecc1f0e from upstream, Fix odd height handling.
  (CVE-2023-51793, bsc#1223272)
* Tue Apr 23 2024 Cliff Zhao <qzhao@suse.com>
- Add ffmpeg-CVE-2023-49502.patch:
  Backport 737ede40 from upstream, account for chroma sub-sampling
  in min size calculation.
  (CVE-2023-49502, bsc#1223235)
* Tue Apr 23 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avfilter-vf_minterpolate-Check-pts-before-division.patch:
  Backport 68146f06 from upstream, Check pts before division.
  (CVE-2023-51798, bsc#1223304)
* Mon Apr 22 2024 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avutil-hwcontext-Don-t-assume-frames_uninit-is-reent.patch:
  Backport 76a48e85 from upstream, Check length.
  (CVE-2024-31578, bsc#1223070)
* Mon Feb 12 2024 Stefan Dirsch <sndirsch@suse.com>
- ffmpeg-avcodec-libdav1d-don-t-repeatedly-parse-the-same-seq.patch
  * fixes build against dav1d, which has been updated in
    SUSE:SLE-15-SP5:Update (where apparently no rebuild of ffmpeg-4
    had been triggered)
* Fri Feb  2 2024 Stefan Dirsch <sndirsch@suse.com>
- no longer build against libmfx; build also 15.5 against libvpl
  (boo#1230983, boo#1219494)
- dropping support for libmfx below covers:
  * libmfx: improper input validation (CVE-2023-48368, bsc#1226897)
  * libmfx: improper buffer restrictions (CVE-2023-45221, bsc#1226898)
  * libmfx: out-of-bounds read (CVE-2023-22656, bsc#1226899)
  * libmfx: out-of-bounds write (CVE-2023-47282, bsc#1226900)
  * libmfx: improper buffer restrictions (CVE-2023-47169, bsc#1226901)
  * Multiple vulnerabilities in the Intel Media SDK (libmfx1) (bsc#1226892)
  * Drop libmfx dependency from our product (jira #PED-10024)
* Tue Dec 26 2023 Jan Engelhardt <jengelh@inai.de>
- Update ffmpeg-glslang-cxx17.patch to build with glslang 14
- Disable vmaf integration as ffmpeg-4 cannot handle vmaf>=3
- Delete vmaf-trim-usr-local.patch
* Wed Dec  6 2023 Jan Engelhardt <jengelh@inai.de>
- Copy codec list from ffmpeg-6
* Fri Nov  3 2023 Marcus Meissner <meissner@suse.com>
- Add ffmpeg-fix-new-binutils.patch:
  Backport 01fc3034 from upstream, Fix build with new binutils
  (bsc#1215309)
* Mon Oct 30 2023 Jan Engelhardt <jengelh@inai.de>
- Add ffmpeg-glslang-cxx17.patch
* Wed Oct  4 2023 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-x86-mathops-clip-constants-used-with-shift-i.patch
  to resolve build failure with binutils >= 2.41. [boo#1215945]
* Tue Jun 27 2023 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-libsvtav1-remove-compressed_ten_bit_format-a.patch
* Thu Apr 27 2023 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-4-CVE-2022-48434.patch:
  Backport d4b7b3c0 from upstream, Fix use after free in
  libavcodec/pthread_frame.c.
  (CVE-2022-48434, bsc#1209934)
* Wed Apr 19 2023 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.4.4:
  * avcodec/012v: Order operations for odd size handling
  * avcodec/alsdec: The minimal block is at least 7 bits
  * avcodec/bink:
  - Avoid undefined out of array end pointers in
    binkb_decode_plane()
  - Fix off by 1 error in ref end
  * avcodec/eac3dec: avoid float noise in fixed mode addition to
    overflow
  * avcodec/eatgq: : Check index increments in tgq_decode_block()
  * avcodec/escape124:
  - Fix signdness of end of input check
  - Fix some return codes
  * avcodec/ffv1dec:
  - Check that num h/v slices is supported
  - Fail earlier if prior context is corrupted
  - Restructure slice coordinate reading a bit
  * avcodec/mjpegenc: take into account component count when
    writing the SOF header size
  * avcodec/mlpdec: Check max matrix instead of max channel in
    noise check
  * avcodec/motionpixels: Mask pixels to valid values
  * avcodec/mpeg12dec: Check input size
  * avcodec/nvenc:
  - Fix b-frame DTS behavior with fractional framerates
  - Fix vbv buffer size in cq mode
  * avcodec/pictordec: Remove mid exit branch
  * avcodec/pngdec: Check deloco index more exactly
  * avcodec/rpzaenc: stop accessing out of bounds frame
  * avcodec/scpr3: Check bx
  * avcodec/scpr: Test bx before use
  * avcodec/snowenc: Fix visual weight calculation
  * avcodec/speedhq: Check buf_size to be big enough for DC
  * avcodec/sunrast: Fix maplength check
  * avcodec/tests/snowenc:
  - Fix 2nd test
  - Return a failure if DWT/IDWT mismatches
  - Unbreak DWT tests
  * avcodec/tiff: Ignore tile_count
  * avcodec/utils:
  - Allocate a line more for VC1 and WMV3
  - Ensure linesize for SVQ3
  - Use 32pixel alignment for bink
  * avcodec/videodsp_template: Adjust pointers to avoid undefined
    pointer things
  * avcodec/vp3: Add missing check for av_malloc
  * avcodec/wavpack:
  - Avoid undefined shift in get_tail()
  - Check for end of input in wv_unpack_dsd_high()
  * avcodec/xpmdec: Check size before allocation to avoid
    truncation
  * avfilter/vf_untile: swap the chroma shift values used for plane
    offsets
  * avformat/id3v2: Check taglen in read_uslt()
  * avformat/mov: Check samplesize and offset to avoid integer
    overflow
  * avformat/mxfdec: Use 64bit in remainder
  * avformat/nutdec: Add check for avformat_new_stream
  * avformat/replaygain: avoid undefined / negative abs
  * swscale/input: Use more unsigned intermediates
  * swscale/output: Bias 16bps output calculations to improve non
    overflowing range
  * swscale: aarch64: Fix yuv2rgb with negative stride
  * Use https for repository links
- Drop patches fixed upstream:
  * ffmpeg-CVE-2022-3964.patch
  * ffmpeg-CVE-2022-3109.patch
  * ffmpeg-CVE-2022-3341.patch
  * ffmpeg-4-CVE-2022-48434.patch
- Use ldconfig_scriptlets macro.
  (CVE-2022-48434, bsc#1209934)
* Thu Mar 16 2023 Jan Engelhardt <jengelh@inai.de>
- Conflict with otherproviders(ffmpeg-tools).
* Fri Jan 20 2023 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2022-3341.patch: Backport from upstream to fix
  null pointer dereference in decode_main_header() in
  libavformat/nutdec.c (bsc#1206778).
* Fri Dec 23 2022 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2022-3109.patch: Backport from upstream to fix
  null pointer dereference in vp3_decode_frame() (bsc#1206442).
* Wed Nov 16 2022 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2022-3964.patch: Backport from upstream to fix
  out of bounds read in update_block_in_prev_frame() (bsc#1205388).
* Mon Oct 10 2022 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.4.3:
  * Stable bug fix release, mainly codecs, filter and format fixes.
  * configure: extend SDL check to accept all 2.x versions (boo#1226308).
- Drop ffmpeg-sdl2-detection.patch: Fixed upstream.
- Refresh patches with quilt:
  * ffmpeg-libglslang-detection.patch
  * ffmpeg-4.2-dlopen-fdk_aac.patch
* Mon Aug 29 2022 Christophe Giboudeaux <christophe@krop.fr>
- Add patch to detect SDL2 >= 2.1.0 (boo#1202848):
  * ffmpeg-sdl2-detection.patch
* Fri Jun 17 2022 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.4.2:
  * Stable bug fix release, mainly codecs, filter and format fixes.
- Refresh ffmpeg-chromium.patch with quilt.
* Wed Mar 23 2022 Jan Engelhardt <jengelh@inai.de>
- Add conflicts for ffmpeg-5's tools
* Thu Mar 17 2022 Enrico Belleri <idesmi@protonmail.com>
- Add ffmpeg-libglslang-detection.patch: detects libglslang
- Enable Vulkan filters
* Sun Mar 13 2022 Predrag Ivanović <predivan@mts.rs>
- Fix OS version check, so nvcodec is enabled for Leap too.
* Wed Feb 16 2022 Dominique Leuenberger <dimstar@opensuse.org>
- Disamble libsmbclient usage (can always be built with
  - -with-smbclient): the usecase of ffmpeg directly accessing
  smb:// shares is quite constructed (most users will have their
  smb shares mounted).
* Sun Jan 16 2022 Callum Farmer <gmbr3@opensuse.org>
- Add ffmpeg-chromium.patch: makes packaging Chromium easier and
  will allow for an easier migration for Chromium to FFmpeg 5
* Tue Nov 30 2021 Dominique Leuenberger <dimstar@opensuse.org>
- Add ffmpeg-4.keyring: properly validate the added gpg signature.
* Thu Oct 28 2021 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.4.1:
  * Stable bug fix release, mainly codecs and format fixes.
- Refresh patches with quilt.
- Drop patches fixed upstream:
  * ffmpeg-CVE-2021-33815.patch
  * ffmpeg-CVE-2021-38114.patch
  * ffmpeg-CVE-2021-38171.patch
  * ffmpeg-CVE-2020-22037.patch
- fix avfilter/vf_yadif: Fix handing of tiny images.
  (CVE-2020-22021, bsc#1186586)
* Sun Sep 26 2021 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2020-22037.patch: Backport from upstream to fix
  denial of service vulnerability exists due to a memory leak in
  avcodec_alloc_context3 at options.c (bsc#1186756).
* Fri Aug 27 2021 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2021-38171.patch: Backport from upstream to fix
  adts_decode_extradata in libavformat/adtsenc.c in FFmpeg 4.4
  does not check the init_get_bits return value (bsc#1189724).
* Tue Aug 10 2021 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2021-38114.patch: Backport from upstream to fix
  the return value of the init_vlc function is not checked
  (bsc#1189142).
* Sat Jul 10 2021 Hans-Peter Jansen <hpj@urpla.net>
- Remove second hunk of ffmpeg-CVE-2020-22046.patch, that contains
  a goto to a none existing label. In order to distinguish this
  patch from the original, I renamed it to
  ffmpeg-4.4-CVE-2020-22046.patch
- While at it, refresh the other patches with offsets
* Thu Jul  8 2021 Alynx Zhou <alynx.zhou@suse.com>
- Add ffmpeg-CVE-2020-22046.patch: Backport from upstream to fix
  a denial of service vulnerability exists in FFmpeg 4.2 due to a
  memory leak in the avpriv_float_dsp_allocl function in
  libavutil/float_dsp.c (bsc#1186849).
- Add ffmpeg-CVE-2021-33815.patch: Backport from upstream to fix
  dwa_uncompress in libavcodec/exr.c in FFmpeg 4.4 allows an
  out-of-bounds array access because dc_count is not strictly
  checked (bsc#1186865).
* Fri Jun  4 2021 Jan Engelhardt <jengelh@inai.de>
- Enable SVT-AV1 encoding
* Thu May 20 2021 Daniel Molkentin <daniel.molkentin@suse.com>
- Enable vulkan on on Leap 15
* Fri Apr 16 2021 Jan Engelhardt <jengelh@inai.de>
- Enable libdavd1 on Leap 15.2+ [boo#1184830]
* Fri Apr  9 2021 Jan Engelhardt <jengelh@inai.de>
- Update to release 4.4
  * New demuxers, AV1 support improvements, and other enhancements.
  * AV1 monochrome encoding support.
- Remove ffmpeg_altivec_yuv2rgb_novsx.patch (merged)
* Sun Mar 14 2021 Dirk Müller <dmueller@suse.com>
- update to 4.3.2:
  * lots of oss-fuzz reported overflow fixes, see included ChangeLog
- drop
    ffmpeg.git-ba3e771a42c29ee02c34e7769cfc1b2dbc5c760a.patch
    0001-lavf-srt-fix-build-fail-when-used-the-libsrt-1.4.1.patch
    0001-avformat-vividas-improve-extradata-packing-checks-in.patch: upstream
* Fri Feb  5 2021 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avformat-vividas-improve-extradata-packing-checks-in.patch
  [boo#1180519] [CVE-2020-35964]
* Sun Jan 24 2021 Dirk Müller <dmueller@suse.com>
- remove dependency on OpenJPEG, this is obsolete since ffmpeg 4.0,
  we already build against OpenJPEG 2.1.
  see changes:
  - Dropped support for OpenJPEG versions 2.0 and below. Using OpenJPEG now
    requires 2.1 (or later) and pkg-config.
* Fri Nov 27 2020 Michel Normand <normand@linux.vnet.ibm.com>
- Add ffmpeg_altivec_yuv2rgb_novsx.patch for ppc64 (BE) as per
  https://trac.ffmpeg.org/ticket/8750
  https://bugzilla.opensuse.org/show_bug.cgi?id=1179332
* Mon Oct 19 2020 Jan Engelhardt <jengelh@inai.de>
- Enable VMAF. This can be used to compute VMAF/PSNR/SSIM.
- Add vmaf-trim-usr-local.patch .
* Wed Oct 14 2020 Jan Engelhardt <jengelh@inai.de>
- Adjust soversion.patch to include a symlink [boo#1177667]
- Add 0001-lavf-srt-fix-build-fail-when-used-the-libsrt-1.4.1.patch
* Mon Jul 27 2020 Hans-Peter Jansen <hpj@urpla.net>
- Apply upstream fix to avoid segfaults in x86/yuv2rgb conversion
  ffmpeg.git-ba3e771a42c29ee02c34e7769cfc1b2dbc5c760a.patch
* Thu Jul 16 2020 Alexander Reimelt <alexander.reimelt@protonmail.ch>
- Add librav1e support
* Sun Jul 12 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.3.1:
  * Stable bug fix release, mainly codecs and format fixes.
* Sat Jul  4 2020 Jan Engelhardt <jengelh@inai.de>
- Add soversion.patch to workaround ELF ABI breakage.
* Wed Jun 17 2020 Jan Engelhardt <jengelh@inai.de>
- Update to release 4.3
  * A plethora of new video filters
  * Intel QSV-accelerated VP9 decoding
  * VDPAU VP9 hwaccel
  * QSV-accelerated VP9 encoding
  * AV1 frame merge bitstream filter
  * AV1 Annex B demuxer
  * Expanded styling support for 3GPP Timed Text Subtitles
  * Support for muxing PCM and PGS in M2TS
- Drop ffmpeg-prefer-dav1d-for-playback.patch
  (solved differently)
- Drop ffmpeg4_swscale_replace_illegal_vector_keyword.patch,
  ffmpeg4_swscale_fix_altivec_vsx_recent_gcc.patch,
  929e5159bc13da374b83f5627879c607acce180b.patch
  (merged)
* Fri Jun  5 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.2.3:
  * Stable bug fix release, mainly codecs and format fixes.
- Drop 0001-avcodec-cbs_jpeg-Check-length-for-SOS.patch: Fixed
  upstream.
* Thu May 28 2020 Jiri Slaby <jslaby@suse.com>
- libfdk-aac is now .so.2, not .so.1.
* Mon May 11 2020 Jan Engelhardt <jengelh@inai.de>
- Throw out v4l2 m2m. This is likely the same case as boo#1041794.
* Thu Apr 30 2020 Matwey Kornilov <matwey.kornilov@gmail.com>
- Enable v4l2 m2m encoders and decoders
* Wed Apr 29 2020 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-cbs_jpeg-Check-length-for-SOS.patch
  [boo#1170767]
* Tue Mar 31 2020 Ismail Dönmez <idonmez@suse.com>
- Add Samba support for Factory (as this needs a fix in Samba itself)
  Add --enable-libsmbclient to configure, add BR on pkgconfig(smbclient)
- License is now GPLv3+ by default (--enable-version3)
* Mon Mar 30 2020 Tomáš Chvátal <tchvatal@suse.com>
- Always build the binary ffmpeg-4 even on Leap releases boo#1167628:
  * The conflicts in place should allow users to decide if they
    want to use ffmpeg from ffmpeg package or ffmpeg-4 from this
    package
* Mon Mar 16 2020 Andreas Schwab <schwab@linux-m68k.org>
- Add -ffat-lto-objects to _lto_cflags to fix configure checks
* Tue Mar  3 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Enable libmfx support for SLE 15 SP2 and Leap 15.2 via
  conditional, libmfx is available there too now.
* Tue Jan 21 2020 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.2.2:
  * Stable bug fix release, mainly codecs and format fixes.
* Fri Jan 10 2020 Ismail Dönmez <idonmez@suse.com>
- Add 929e5159bc13da374b83f5627879c607acce180b.patch to fix
  bad ID3v2 tag length.
* Mon Dec 30 2019 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Drop unused liboil BuildRequires.
* Wed Sep 18 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.2.1:
  * Stable bug fix release, mainly codecs and format fixes.
- Drop upstream fixed patch:
  0001-avcodec-h2645_parse-zero-initialize-the-rbsp-buffer.patch
* Tue Sep 10 2019 Jan Engelhardt <jengelh@inai.de>
- Add 0001-avcodec-h2645_parse-zero-initialize-the-rbsp-buffer.patch
  [boo#1149839, CVE-2019-15942]
* Wed Sep  4 2019 Ismail Dönmez <idonmez@suse.com>
- Make ffmpeg-4.2-dlopen-fdk_aac.patch less verbose
* Thu Aug 22 2019 Ismail Dönmez <idonmez@suse.com>
- Rename ffmpeg-4.2-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
  to ffmpeg-4.2-dlopen-fdk_aac.patch since we need dlopen only
  for fdk_aac and looks like some other parts of the patch is
  buggy.
* Thu Aug 22 2019 Ismail Dönmez <idonmez@suse.com>
- Sync ffmpeg-4.2-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
  from upstream.
* Sun Aug 18 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Disable LTO for arm, fixes build.
* Wed Aug 14 2019 Michel Normand <normand@linux.vnet.ibm.com>
- avoid ppc64le build error upstream issue
  https://trac.ffmpeg.org/ticket/7861
  Add ffmpeg4_swscale_replace_illegal_vector_keyword.patch
  Add ffmpeg4_swscale_fix_altivec_vsx_recent_gcc.patch
* Mon Aug 12 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add ffmpeg-prefer-dav1d-for-playback.patch: Prefer using dav1d
  for av1 playback over libaom.
* Tue Aug  6 2019 Ismail Dönmez <idonmez@suse.com>
- Update to FFmpeg 4.2 "Ada"
  * tpad filter
  * AV1 decoding support through libdav1d
  * dedot filter
  * chromashift and rgbashift filters
  * freezedetect filter
  * truehd_core bitstream filter
  * dhav demuxer
  * PCM-DVD encoder
  * GIF parser
  * vividas demuxer
  * hymt decoder
  * anlmdn filter
  * maskfun filter
  * hcom demuxer and decoder
  * ARBC decoder
  * libaribb24 based ARIB STD-B24 caption support (profiles A and C)
  * Support decoding of HEVC 4:4:4 content in nvdec and cuviddec
  * removed libndi-newtek
  * agm decoder
  * KUX demuxer
  * AV1 frame split bitstream filter
  * lscr decoder
  * lagfun filter
  * asoftclip filter
  * Support decoding of HEVC 4:4:4 content in vdpau
  * colorhold filter
  * xmedian filter
  * asr filter
  * showspatial multimedia filter
  * VP4 video decoder
  * IFV demuxer
  * derain filter
  * deesser filter
  * mov muxer writes tracks with unspecified language instead
    of English by default
  * added support for using clang to compile CUDA kernels
  * avcodec/g729_parser: Check channels (CVE-2022-1475, bsc#1198898)
- Drop ffmpeg-avcodec-libdav1d-AV1-decoder-wrapper.patch, merged
  upstream.
- Rebase and rename
  ffmpeg-4.1-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
  to
  ffmpeg-4.2-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
- See /usr/share/doc/packages/ffmpeg-4/Changelog for the complete
  changelog.
* Wed Jul 31 2019 Ismail Dönmez <idonmez@suse.com>
- Update to version 4.1.4
  * See /usr/share/doc/packages/ffmpeg-4/Changelog for the complete
    changelog.
* Sat Jul  6 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add pkgconfig(libva-drm), pkgconfig(libva-x11) BuildRequires: and
  conditional pkgconfig(libmfx) BuildRequires: Build intel-mediasdk
  support when possible.
* Tue Jul  2 2019 Ismail Dönmez <idonmez@suse.com>
- Add back pkgconfig(fdk-aac) BuildRequires since we still need
  the headers at compile time.
- Fix include paths in
  ffmpeg-4.1-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
* Tue Jun 11 2019 Ismail Dönmez <idonmez@suse.com>
- Add ffmpeg-4.1-dlopen-faac-mp3lame-opencore-x264-x265-xvid.patch
  from OpenMandriva to optionally enable runtime enabling of
  fdkaac/lame/x264/x265
- Enable runtime enabling for fdkaac via --enable-libfdk-aac-dlopen
- Rename bcond fdk_aac to fdk_aac_dlopen
- Remove fdk-aac BuildRequires now it's only dlopen'd
* Tue May 14 2019 Martin Liška <mliska@suse.cz>
- Enable LTO for all except i586 (boo#1133123).
* Sun May  5 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Disable LTO again, as it breaks build for i586 (boo#1133123).
* Fri May  3 2019 Jan Engelhardt <jengelh@inai.de>
- Throw out svt-av1. The build is unable to complete
  in openSUSE:Factory.
* Thu May  2 2019 Martin Liška <mliska@suse.cz>
- Use %%make_build in order to provide parallel build for tools/*.
  And make output verbose.
* Thu May  2 2019 Martin Liška <mliska@suse.cz>
- Enable LTO for new SUSE versions (boo#1133123).
* Tue Apr 30 2019 Hans-Peter Jansen <hpj@urpla.net>
- Update patch 0001-Add-ability-for-ffmpeg-to-run-svt-av1.patch
  from upstream
* Tue Apr  2 2019 seanlew@opensuse.org
- Update to version 4.1.3:
  * Updates and bug fixes for codecs, filters and formats.
    [boo#1133153, boo#1133155, CVE-2019-11338, CVE-2019-11339]
* Thu Mar 28 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Update to version 4.1.2:
  * Updates and bug fixes for codecs, filters and formats.
* Sun Mar 17 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add ffmpeg-avcodec-libdav1d-AV1-decoder-wrapper.patch: Backport
  dav1d decoder support for aom (av1) codec. Following this, add
  conditional pkgconfig(dav1d) BuildRequires and pass conditional
  - -enable-libdav1d to configure. Also add libdav1d to
  enable_decoders.
* Sat Mar  9 2019 Bjørn Lie <bjorn.lie@gmail.com>
- Add a new filter line to rpmlintrc
  (addFilter("no-dependency-on ffmpeg-4-lib*")).
* Mon Mar  4 2019 John Vandenberg <jayvdb@gmail.com>
- Add trivial encoder rawvideo, already enabled in decoders
* Sat Mar  2 2019 Jan Engelhardt <jengelh@inai.de>
- Unconditionalize bs2b, it exists in openSUSE 13.x too.
* Fri Mar  1 2019 bjorn.lie@gmail.com
- Drop ffmpeg-libcdio_cdda-pkgconfig.patch: It only adds comments
  in it's current form, so serves no purpose at all anymore.
- Refresh patches with refresh_patches service.
- Rename rpmlintrc file to ffmpeg-4-rpmlintrc.
* Thu Feb 28 2019 bjorn.lie@gmail.com
- Add missing conditional configure option: --enable-libbs2b,
  BuildRequires already in place.
* Sat Feb 16 2019 bjorn.lie@gmail.com
- Add aac to enabled_encoders and enabled_decoders. Build the
  native aac support in ffmpeg. These do not support HE-AAC (v1/2)
  protocols.
* Sat Feb 16 2019 davejplater@gmail.com
- Update 0001-Add-ability-for-ffmpeg-to-run-svt-av1.patch from git
  To fix build with SVT-AV1.
* Tue Feb 12 2019 bjorn.lie@gmail.com
- Update to version 4.1.1:
  * Various filter and codec fixes and enhancements.
  * configure: Add missing xlib dependency for VAAPI X11 code.
  * For complete changelog, see
    /usr/share/doc/packages/ffmpeg-4/Changelog
* Tue Feb  5 2019 Adrian Schröter <adrian@suse.de>
- enable AV1 support on x86_64
  * requires patch 0001-Add-ability-for-ffmpeg-to-run-svt-av1.patch
- refreshed all patches
* Tue Jan 15 2019 bjorn.lie@gmail.com
- Add conditional pkgconfig(vo-amrwbenc) BuildRequires and
  conditionally pass --enable-libvo-amrwbenc --enable-version3 to
  configure: build amrwb encoder if dependency is present.
* Wed Dec  5 2018 Stefan Brüns <stefan.bruens@rwth-aachen.de>
- Enable encoding/decoding with nvcodec, the required headers are already
  in TW (permissively licensed). The required NVidia libraries are dlopen'ed.
- Enable ILBC decoder, ilbc is free and already packaged standalone.
* Tue Nov  6 2018 sean@suspend.net
- Update ffmpeg to 4.1
  * Lots of filter updates as usual: deblock, tmix, aplify,
    fftdnoiz, aderivative, aintegral, pal75bars, pal100bars,
    adeclick, adeclip, lensfun (wrapper), colorconstancy, 1D LUT
    filter (lut1d), cue, acue, transpose_npp, amultiply,
    Block-Matching 3d (bm3d) denoising filter, acrossover filter,
    audio denoiser as afftdn filter, sinc audio filter source,
    chromahold, setparams, vibrance, xstack,
    (a)graphmonitor filter yadif_cuda filter.
  * AV1 parser
  * Support for AV1 in MP4
  * PCM VIDC decoder and encoder
  * libtensorflow backend for DNN based filters like srcnn
  * -- The following only enabled in third-party builds:
  * ATRAC9 decoder
  * AVS2 video decoder via libdavs2
  * IMM4 video decoder
  * Brooktree ProSumer video decoder
  * MatchWare Screen Capture Codec decoder
  * WinCam Motion Video decoder
  * RemotelyAnywhere Screen Capture decoder
  * AVS2 video encoder via libxavs2
  * ILBC decoder
  * SER demuxer
  * Decoding S12M timecode in H264
  * For complete changelog, see https://git.ffmpeg.org/gitweb/ffmpeg.git/shortlog/n4.1
- Remove 0001-avcodec-libaom-fix-setting-amount-of-threads.patch
  (fixed upstream (bsc#776cdd1), remove ffmpeg-CVE-2018-13305.patch,
  remove 0001-avformat-flvenc-Check-audio-packet-size.patch,
  remove cve-2017-17555.diff (fixed upstream).
* Sat Nov  3 2018 sean@suspend.net
- Remove 0001-avformat-fivenc-Check-audio-packet-size.patch (fixed upstream (bsc#8591d16)
- Update ffmpeg to 4.0.3
  * For complete changelog, see https://git.ffmpeg.org/gitweb/ffmpeg.git/shortlog/n4.0.3
* Tue Oct 23 2018 qzheng@suse.com
- Add ffmpeg-CVE-2018-13305.patch to add a missing check for
  negative values of mqaunt variable (CVE-2018-13305,
  bsc#1100345).
* Thu Sep 13 2018 9+suse@cirno.systems
- Add 0001-avcodec-libaom-fix-setting-amount-of-threads.patch
* Fri Aug 24 2018 jengelh@inai.de
- Add 0001-avformat-flvenc-Check-audio-packet-size.patch
  [CVE-2018-15822, boo#1105869]
* Mon Aug 13 2018 bjorn.lie@gmail.com
- Update to version 4.0.2:
  * CVE-2018-13300: out of array read (boo#1100348, CVE-2018-13300)
  * Various bugfixes and a revert
* Sat Aug 11 2018 carmen@carmenbianca.eu
- bsc#1092241 Enable webvtt encoders and decoders.
* Tue Aug  7 2018 bjorn.lie@gmail.com
- Build codec2 encoder and decoder, add libcodec2 to
  enable_decoders and enable_encoders.
* Mon Aug  6 2018 davejplater@gmail.com
- Enable mpeg 1 and 2 encoders.
* Sun Aug  5 2018 bjorn.lie@gmail.com
- Add conditional pkgconfig(aom) BuildRequires and pass
  - -enable-libaom to configure as well as add libaom and libaom_av1
  to enable_decoders and enable_encoders: Build AOMedia Video 1
  (AV1) support.
* Tue Jul 31 2018 tchvatal@suse.com
- bsc#1103064 attempt to allow migration from the unprefixed devel
  packages cleanly
* Fri Jul 27 2018 tchvatal@suse.com
- Reduce the optional conditional for the SLE12 backports to
  cover everything, most of the packages in old codestreams were
  not really ready as they need additional baselibs/etc.
  * Since these are new features user will simply wait or use TW
* Fri Jul 27 2018 jengelh@inai.de
- Enable "kmsgrab" input device
* Thu Jul 26 2018 tchvatal@suse.com
- Redo the nvidia condition based on review feeback
* Wed Jul 25 2018 tchvatal@suse.com
- Do not condition nvidia based on BUILD_ORIG all the support is in
  TW only and not on different instances as such safeguard it with
  version check only bsc#1102532
* Wed Jul 18 2018 tchvatal@suse.com
- Add new bconds to build on SLE12 backports project without
  requiring extra packages:
  * %%bcond_without codec2
  * %%bcond_without bs2b
  * %%bcond_without lv2
  * %%bcond_without rubberband
  * %%bcond_without soxr
  * %%bcond_without zmq
* Fri Jul  6 2018 tchvatal@suse.com
- Fix typo in swresample name
* Wed Jul  4 2018 tchvatal@suse.com
- Conditionalize full build to be primary only on Leap15+
* Tue Jul  3 2018 tchvatal@suse.com
- Add macros to allow conflicting with all other devel projects
  to ensure we always install only one specific ffmpeg
* Sat Jun 30 2018 tchvatal@suse.com
- Conditionalize the vidstab build to not pull it on old releases
- Conditionalize srt support to not pull it on older releases
  - ------------------------------------------------------------------
* Fri Jun 29 2018 9+suse@cirno.systems
- Enable ffnvcodec when building with NVIDIA support
* Fri Jun 29 2018 bjorn.lie@gmail.com
- Add pkgconfig(srt) BuildRequires and pass --enable-libsrt to
  configure, enable srt support.
- Refresh patches with quilt:
  * cve-2017-17555.diff
  * ffmpeg-codec-choice.diff
  * ffmpeg-libcdio_cdda-pkgconfig.patch
  * ffmpeg-new-coder-errors.diff
* Fri Jun 29 2018 9+suse@cirno.systems
- Enable libxml2 (used by MPEG DASH demuxer)
* Wed Jun 27 2018 jengelh@inai.de
- Update to new upstream release 4.0.1
  * Fixed some integer overflows, undefined shifts, negative
    shifts, division by 0, and a null pointer deref.
* Mon Jun 18 2018 bjorn.lie@gmail.com
- Enable pkgconfig(vidstab) BuildRequires unconditionally, now
  available in openSUSE.
* Thu Jun 14 2018 tchvatal@suse.com
- Conditionalize openmpt build to be resolvable on Leap 42.3
* Thu Jun 14 2018 tchvatal@suse.com
- Conditionalize mysofa build to be resolvable on Leap 15
* Thu Jun 14 2018 tchvatal@suse.com
- Conditionalize zimg to build on Leap 42.3
* Thu Jun 14 2018 tchvatal@suse.com
- Use autopatch
* Wed Jun 13 2018 tchvatal@suse.com
- Provide ffmpeg symbol without version on main package too
* Wed Jun 13 2018 tchvatal@suse.com
- Prefix all the devel packages and conflict between releases
  * Provide always the %%version-%%release of the respective build
* Wed Jun 13 2018 tchvatal@suse.com
- Fix setup call to enter to proper folder
* Wed Jun 13 2018 tchvatal@suse.com
- Conflict with other ffmpeg-devel packages, simply always pull
  one of them
* Wed Jun 13 2018 tchvatal@suse.com
- Move license markings to the libs itself
- Add condition to switch between full build and lib only one
- Add provides/obsoletes on the ffmpeg private headers
* Sat Jun  2 2018 9+suse@cirno.systems
- Reintroduce conditional libxvid support since FFmpeg’s
  MPEG4-ASP encoder is not quite up to par
* Mon May 28 2018 jengelh@inai.de
- Avoid double-nesting BUILD_ORIG with %%withs.
  (Reintroduces with_opencore)
* Sun May 27 2018 bjorn.lie@gmail.com
- Drop long obsolete and unused vo_aacenc %%bcond_with.
- Add conditional --enable-librtmp in build_orig part of spec,
  conditional BuildRequires already in place.
- Drop opencore conditional, explicitly enable them for all
  BUILD_ORIG builds.
- Drop conditional xvid %%bcond_with, libxvidcore-devel
  BuildRequires and --enable-libxvid call to configure: ffmpeg have
  a fully capable mpeg4 encoder and decoder, avoid external
  dependency.
- Minor spec cleanup.
* Fri Apr 27 2018 9+suse@cirno.systems
- Enable libmysofa support (sofalizer HRTF filter)
* Wed Apr 25 2018 9+suse@cirno.systems
- Remove superfluous __DATE__/__TIME__ replacement
- Correct libvpx version dependency
- Enable support for additional libraries:
  * libbs2b
  * libcodec2
  * libfontconfig
  * libfribidi (already in BuildRequires)
  * libgme
  * libjack (already in BuildRequires)
  * libopenmpt
  * librubberband
  * libsoxr
  * libssh
  * libv4l2
  * libzmq
  * lv2
* Sat Apr 21 2018 jengelh@inai.de
- Update to new upstream release 4.0
  * New audio filters: mcompand, acontrast, lv2 wrapper, hilbert,
    aiir, drmeter
  * New video filters: mix, normalize, fillborders, setrange,
    deconvolve, entropy, vfrdet
  * OpenCL overlay filter
  * VAAPI MJPEG and VP8 decoding
  * VAAPI-accelerated ProcAmp (color balance), denoise and
    sharpness filters
  * Removed the ffserver program
  * Removed the ffmenc and ffmdec muxer and demuxer
  * codec2 en/decoding via libcodec2
  * New bitstream filter: hapqa_extract, filter_units
  * Fixed img2dec infinite loop [boo#1090826, CVE-2018-7751]
- Remove 0001-opusenc-psy-disable-stereo-searches.patch
* Mon Apr  9 2018 enzokiel@kabelmail.de
- Enable build against libzimg.
* Tue Mar 27 2018 jengelh@inai.de
- Add 0001-opusenc-psy-disable-stereo-searches.patch
  to fix a crash in the Opus encoder when outputting mono.
- Enable FFmpeg Opus encoder as a selectable runtime alternative
  to Xiph libopus.
* Fri Mar 23 2018 alarrosa@suse.com
- Create a new package ffmpeg-private-devel which contains some
  headers under /usr/include/ffmpeg/private that were not installed
  by upstream. Those headers are needed by the libav package in order
  to build avconv and other tools using the libav* libraries generated
  by ffmpeg instead of its own. No other package should require
  ffmpeg-private-devel.
* Wed Mar 21 2018 alarrosa@suse.com
- Build and install also the sidxindex tool
* Tue Feb 20 2018 bjorn.lie@gmail.com
- Enable mpeg1video and mpeg2video in enable_decoders, and remove
  it from disable-decoders call given to configure, mpeg2 now
  available in openSUSE.
* Tue Feb 13 2018 nico.kruber@gmail.com
- enable video stabilization/deshaking via libvidstab (optional)
* Mon Feb 12 2018 jengelh@inai.de
- Update to new bugfix release 3.4.2
  * Fix integer overflows, multiplication overflows, undefined
    shifts, and verify buffer lengths.
  * avfilter/vf_transpose: Fix used plane count
    [boo#1078488, CVE-2018-6392]
  * avcodec/utvideodec: Fix bytes left check in decode_frame()
    [boo#1079368, CVE-2018-6621]
- Enable use of libzvbi for displaying teletext subtitles.
- Fixed a DoS in swri_audio_convert(), added cve-2017-17555.diff
  [boo#1072366, CVE-2017-17555].
* Mon Dec 11 2017 jengelh@inai.de
- Update to new bugfix release 3.4.1
  * Fixed integer overflows, division by zero, illegal bit shifts
  * Fixed the gmc_mmx function which failed to validate width
    and height [boo#1070762, CVE-2017-17081]
  * Fixed out-of-bounds in VC-2 encoder [boo#1069407, CVE-2017-16840]
  * ffplay: use SDL2 audio API
- Removed 0001-avcodec-x86-mpegvideodsp-Fix-signedness-bug-in-need_.patch
  (upstreamed).
* Fri Dec  1 2017 jengelh@inai.de
- Add 0001-avcodec-x86-mpegvideodsp-Fix-signedness-bug-in-need_.patch
  [boo#1070762]
* Thu Nov 30 2017 jslaby@suse.com
- install also doc/ffserver.conf
* Tue Oct 31 2017 jengelh@inai.de
- Get rid of ffmpeg-pkgconfig-version.patch.
* Mon Oct 16 2017 jengelh@inai.de
- Update to new upstream release 3.4
  * New video filters: deflicker, doublewave, lumakey, pixscope,
    oscilloscope, robterts, limiter, libvmaf, unpremultiply,
    tlut2, floodifll, pseudocolor, despill, convolve, vmafmotion.
  * New audio filters: afir, crossfeed, surround, headphone,
    superequalizer, haas.
  * Some video filters with several inputs now use a common set
    of options: blend, libvmaf, lut3d, overlay, psnr, ssim. They
    must always be used by name.
  * librsvg support for svg rasterization
  * spec-compliant VP9 muxing support in MP4
  * Remove the libnut and libschroedinger muxer/demuxer wrappers
  * drop deprecated qtkit input device (use avfoundation instead)
  * SUP/PGS subtitle muxer
  * VP9 tile threading support
  * KMS screen grabber
  * CUDA thumbnail filter
  * V4L2 mem2mem HW assisted codecs
  * Rockchip MPP hardware decoding
  * (Not in openSUSE builds, only original ones:)
  * Gremlin Digital Video demuxer and decoder
  * Additional frame format support for Interplay MVE movies
  * Dolby E decoder and SMPTE 337M demuxer
  * raw G.726 muxer and demuxer, left- and right-justified
  * NewTek NDI input/output device
  * FITS demuxer, muxer, decoder and encoder
- Fixed a double free in huffyuv [boo#1064577, CVE-2017-15186]
- Fixed an out-of-bounds in ffv1dec [boo#1066428, CVE-2017-15672]
- Fixed a denial of service in rtmppkt [boo#1082335, CVE-2017-11665]
* Tue Sep 12 2017 jengelh@inai.de
- Update to new upstream release 3.3.4.
  * avutil/pixdesc: fixed NULL deref in av_color_primaries_name
    [CVE-2017-14225] [boo#1058018]
  * avformat/asfdec: Fix DoS in asf_build_simple_index
    [CVE-2017-14223] [boo#1058019]
  * avformat/mov: Fix DoS in read_tfra
    [CVE-2017-14222] [boo#1058020].
- Dropped integrated patches:
  D 0001-avformat-hls-Fix-DoS-due-to-infinite-loop.patch
  D 0001-avformat-nsvdec-Fix-DoS-due-to-lack-of-eof-check-in-.patch
  D 0002-avformat-asfdec-Fix-DoS-due-to-lack-of-eof-check.patch
  D 0002-avformat-mxfdec-Fix-DoS-issues-in-mxf_read_index_ent.patch
  D 0003-avformat-cinedec-Fix-DoS-due-to-lack-of-eof-check.patch
  D 0003-avformat-mxfdec-Fix-Sign-error-in-mxf_read_primer_pa.patch
  D 0004-avformat-rmdec-Fix-DoS-due-to-lack-of-eof-check.patch
  D 0005-avformat-rl2-Fix-DoS-due-to-lack-of-eof-check.patch
  D 0006-avformat-mvdec-Fix-DoS-due-to-lack-of-eof-check.patch
* Thu Sep  7 2017 jengelh@inai.de
- Add 0001-avformat-nsvdec-Fix-DoS-due-to-lack-of-eof-check-in-.patch
  [CVE-2017-14171] [boo#1057539],
  0002-avformat-mxfdec-Fix-DoS-issues-in-mxf_read_index_ent.patch
  [CVE-2017-14170] [boo#1057537],
  0003-avformat-mxfdec-Fix-Sign-error-in-mxf_read_primer_pa.patch
  [CVE-2017-14169] [boo#1057536]
* Mon Sep  4 2017 jengelh@inai.de
- Add 0001-avformat-hls-Fix-DoS-due-to-infinite-loop.patch
  [CVE-2017-14058] [boo#1056762],
  0002-avformat-asfdec-Fix-DoS-due-to-lack-of-eof-check.patch
  [CVE-2017-14057] [boo#1056761],
  0003-avformat-cinedec-Fix-DoS-due-to-lack-of-eof-check.patch
  [CVE-2017-14059] [boo#1056763],
  0004-avformat-rmdec-Fix-DoS-due-to-lack-of-eof-check.patch
  [CVE-2017-14054] [boo#1056765],
  0005-avformat-rl2-Fix-DoS-due-to-lack-of-eof-check.patch
  (code not enabled in openSUSE, though in packman)
  [CVE-2017-14056] [boo#1056760],
  0006-avformat-mvdec-Fix-DoS-due-to-lack-of-eof-check.patch
  [CVE-2017-14055] [boo#1056766]
* Sat Aug 26 2017 jengelh@inai.de
- Unconditionalize celt, ass, openjpeg, webp, netcdf, libva, vdpau.
* Fri Aug 25 2017 olaf@aepfle.de
- Build unconditionally with lame and twolame
* Sun Jul 30 2017 jengelh@inai.de
- Update to maintenance release 3.3.3
  * Various fixes for integer overflows, too-large bit shifts
    and buffer length checks.
- Drop 0001-avcodec-apedec-Fix-integer-overflow.patch
  (included upstream)
* Tue Jul 18 2017 jengelh@inai.de
- Add 0001-avcodec-apedec-Fix-integer-overflow.patch
  to address CVE-2017-11399 [boo#1049095]
* Fri Jun 23 2017 davejplater@gmail.com
- Enabled cuda and cuvid for unrestricted build.
- Fixed typos in devel package descriptions.
* Wed Jun  7 2017 jengelh@inai.de
- Update to new upstream release 3.3.2
  * Various fixes for integer overflows and too-large bit shifts
* Wed May 31 2017 davejplater@gmail.com
- Disable cuda support to fix boo#1041794:
  ffmpeg 3.3. enablement of cuda prevents H264/avc1.4d400d videos
  from playing on Youtube
- Refreshed patches: ffmpeg-codec-choice.diff
  ffmpeg-libcdio_cdda-pkgconfig.patch
  ffmpeg-pkgconfig-version.patch and ffmpeg-new-coder-errors.diff
* Wed May 31 2017 jengelh@inai.de
- Add additional checks to ensure MPEG is off
* Fri May 19 2017 jengelh@inai.de
- Update to new upstream release 3.3.1
  * Fix uninitialized variables, signed integer overflow,
    excess shift operations. Add boundary checks.
* Tue Apr 18 2017 jengelh@inai.de
- Enable ac3 per request from idonmez
* Fri Apr 14 2017 jengelh@inai.de
- Update to new upstream release 3.3
  * EBU R128 implementation now within ffmpeg, not relying on
    external library anymore
  * New video filters "premultiply", "readeia608", "threshold",
    "midequalizer"
  * Support for spherical videos
  * New decoders: 16.8 and 24.0 floating point PCM, XPM
  * New demuxers: MIDI Sample Dump Standard, Sample Dump eXchange demuxer
  * MJPEG encoding uses Optimal Huffman tables now
  * Native Opus encoder
  * Support .mov with multiple sample description tables
  * Removed the legacy X11 screen grabber, use XCB instead
  * Removed asyncts filter (use af_aresample instead)
  * resolved CVE-2016-10190 [boo#1022920],
    CVE-2016-10191 [boo#1022921], CVE-2016-10192 [boo#1022922],
    CVE-2017-7859 [boo#1034183], CVE-2017-7862 [boo#1034181],
    CVE-2017-7863 [boo#1034179], CVE-2017-7865 [boo#1034177],
    CVE-2017-7866 [boo#1034176]
* Thu Apr 13 2017 idonmez@suse.com
- Enable mp3 decoding
* Sat Feb 18 2017 dimstar@opensuse.org
- Have libavcodec57 additionally provide libavcodec57(unrestricted)
  when building unrestricted: allow third party packages to require
  the unrestricted codec. The existing -full provides is not
  suitable as it can be provided by multiple libavcodec* packages,
  whereas we require a specific ABI version.
* Sat Feb 11 2017 jengelh@inai.de
- Update to new upstream release 3.2.4
  * lavf/mov.c: Avoid heap allocation wrap in mov_read_hdlr
  * lavf/mov.c: Avoid OOB in mov_read_udta_string()
  * lavf/mov.c: Avoid heap allocation wraps in mov_read_{senc,saiz}()
* Sat Feb 11 2017 olaf@aepfle.de
- Make sure each subpkg comes from the same src.rpm
* Tue Feb  7 2017 jengelh@inai.de
- Update to new upstream release 3.2.3
  * Maintenance release with bugfixes
  * ffplay: fix sws_scale possible out of bounds array access
- Drop version number from patch: ffmpeg-2.4.5-arm6l.patch ->
  ffmpeg-arm6l.diff
* Tue Jan  3 2017 olaf@aepfle.de
- Wrap netcdf support in build condtional because it is a drop-in pkg
* Tue Dec 20 2016 tchvatal@suse.com
- Enable all muxers and demuxers as they are just descriptor of format
  thus do not change the behaviour in any relevant way.
  * The best user now gets is proper interpretation of the format and
    failure to play it without proper de/encoder
  * Recommended by vlc team to be done this way :)
* Tue Dec  6 2016 jengelh@inai.de
- Update to new upstream release 3.2.2
  * avformat/rtmppkt: Check for packet size mismatches
  * avcodec/flacdec: Fix undefined shift in decode_subframe()
  * avcodec/flacdec: Fix signed integer overflow in
    decode_subframe_fixed()
  * avcodec/flacdsp_template: Fix undefined shift in
    flac_decorrelate_indep_c
* Sat Nov 26 2016 aloisio@gmx.com
- Update to version 3.2.1:
  * avcodec/aac_adtstoasc_bsf: validate and forward extradata
    if the stream is already ASC
  * libopusdec: default to stereo for invalid number of
    channels
  * sbgdec: prevent NULL pointer access
  * rmdec: validate block alignment
  * smacker: limit recursion depth of smacker_decode_bigtree
  * mxfdec: fix NULL pointer dereference in mxf_read_packet_old
  * ffmdec: validate codec parameters
  * avformat/mpeg: Adjust vid probe threshold to correct
    mis-detection
  * avcodec/avpacket: fix leak on realloc in
    av_packet_add_side_data()
  * avformat/apngenc: use the stream parameters extradata if
    available
  * ffprobe: fix crash in case -of is specified with an empty
    string
  * exr: fix out-of-bounds read
  * libschroedingerdec: fix leaking of framewithpts
  * filmstripdec: correctly check image dimensions
  * icodec: fix leaking pkt on error
  * dvbsubdec: fix division by zero in compute_default_clut
  * escape124: reject codebook size 0
  * mpegts: prevent division by zero
  * matroskadec: fix NULL pointer dereference in
    webm_dash_manifest_read_header
  * mxfdec: fix NULL pointer dereference
  * avcodec/mpeg4videodec: Workaround interlaced mpeg4 edge MC
    bug
  * avcodec/mpegvideo: Fix edge emu buffer overlap with
    interlaced mpeg4
  * avcodec/ituh263dec: Avoid spending a long time in slice
    sync
  * avcodec:  Check side data size before use
  * avformat/flvdec: Fix regression losing streams
* Fri Oct 28 2016 jengelh@inai.de
- Update to new upstream release 3.2
  * SDL2 output device and ffplay support
  * SDL1 output device and SDL1 support removed
  * New: libopenmpt demuxer, fifo muxer, True Audio (TTA) muxer
  * New filters: weave, gblur, avgblur, sobel, prewitt,
  vaguedenoiser, yuvtestsrc, lut2, hysteresis, maskedclamp,
  crystalizer, acrusher, bitplanenoise, sidedata, asidedata
  * Non-Local Means (nlmeans) denoising filter
  * 16-bit support in curves filter and selectivecolor filter
  * Added threads option per filter instance
  * The "curves" filter does not automatically insert points at x=0
  and x=1 anymore
  * Matroska muxer now writes CRC32 elements by default in all
  Level 1 elements
  * New "tee" protocol
  * VP8 in Ogg muxing
  * Floating point support in ALS decoder
  * Extended mov edit list support
  * Changed mapping of RTP MIME type G726 to codec g726le.
- Drop ffmpeg-fix-CONFIG_VC1DSP-changes.patch
  (no longer needed)
* Fri Oct 28 2016 olaf@aepfle.de
- Enable libfdk_aac if it is available at buildtime
* Sat Oct 22 2016 aloisio@gmx.com
- Update to version 3.1.5
  * avformat/mxfdec: Check size to avoid integer overflow in
    mxf_read_utf16_string()
  * avcodec/mpegvideo_enc: Clear mmx state in
    ff_mpv_reallocate_putbitbuffer()
  * avcodec/utils: Clear MMX state before returning from
    avcodec_default_execute*()
  * libopenjpegenc: fix out-of-bounds reads when filling the
    edges
  * libopenjpegenc: stop reusing image data buffer for
    openjpeg 2
  * avformat/utils: Update codec_id before using it in the
    parser init
  * ffmpeg: remove unused and errorneous AVFrame timestamp
    check
  * Support for MIPS cpu P6600
  * avutil/mips/generic_macros_msa: rename macro variable
    which causes segfault for mips r6
* Sat Oct  1 2016 aloisio@gmx.com
- Update to version 3.1.4
  * avformat/avidec: Check nb_streams in read_gab2_sub()
  * avformat/avidec: Remove ancient assert
  * avfilter/vf_colorspace: fix range for output colorspace
    option
  * lavc/mediacodecdec_h264: fix SODB escaping
  * avcodec/nvenc: fix const options for hevc gpu setting
  * avformat/avidec: Fix memleak with dv in avi
  * lavc/movtextdec.c: Avoid infinite loop on invalid data.
  * avcodec/ansi: Check dimensions
  * avcodec/cavsdsp: use av_clip_uint8() for idct
  * avformat/movenc: Check packet in mov_write_single_packet()
    too
  * avformat/movenc: Factor check_pkt() out
  * avformat/utils: fix timebase error in avformat_seek_file()
  * avcodec/g726: Add missing ADDB output mask
  * avcodec/avpacket: clear side_data_elems
  * avformat/movenc: Check first DTS similar to dts difference
  * avcodec/ccaption_dec: Use simple array instead of AVBuffer
  * avcodec/svq3: Reintroduce slice_type
  * avformat/mov: Fix potential integer overflow in
    mov_read_keys
  * swscale/swscale_unscaled: Try to fix
    Rgb16ToPlanarRgb16Wrapper() with slices
  * swscale/swscale_unscaled: Fix packed_16bpc_bswap() with
    slices
  * avformat/avidec: Fix infinite loop in avi_read_nikon()
  * lavf/utils: Avoid an overflow for huge negative durations.
  * avformat/hls: Fix handling of EXT-X-BYTERANGE streams over
    2GB
  * lavc/avpacket: Fix undefined behaviour, do not pass a null
    pointer to memcpy().
  * lavc/mjpegdec: Do not skip reading quantization tables.
  * cmdutils: fix implicit declaration of SetDllDirectory
    function
* Mon Aug 29 2016 stefan.bruens@rwth-aachen.de
- Fix linking errors for arm and aarch64 builds, boo#995937
  * Add ffmpeg-fix-CONFIG_VC1DSP-changes.patch
* Sat Aug 27 2016 aloisio@gmx.com
- Update to version 3.1.3
  * examples/demuxing_decoding: convert to codecpar
  * avcodec/exr: Check tile positions
  * avcodec/aacenc: Tighter input checks
  * avformat/wtvdec: Check pointer before use
  * libavcodec/wmalosslessdec: Check the remaining bits
  * avcodec/adpcm: Fix adpcm_ima_wav padding
  * avcodec/svq3: fix slice size check
  * avcodec/diracdec: Check numx/y
  * avcodec/h2645_parse: fix nal size
  * avcodec/h2645_parse: Use get_nalsize() in
    ff_h2645_packet_split()
  * h2645_parse: only read avc length code at the correct
    position
  * h2645_parse: don't overread AnnexB NALs within an avc
    stream
  * avcodec/h264_parser: Factor get_avc_nalsize() out
  * avcodec/cfhd: Increase minimum band dimension to 3
  * avcodec/indeo2: check ctab
  * avformat/swfdec: Fix inflate() error code check
  * avcodec/rawdec: Fix bits_per_coded_sample checks
  * vcodec/h2645_parse: Clear buffer padding
  * avcodec/h2645: Fix NAL unit padding
  * avfilter/drawutils: Fix single plane with alpha
  * cmdutils: check for SetDllDirectory() availability
* Tue Aug  9 2016 aloisio@gmx.com
- Update to version 3.1.2:
  * avcodec/rawdec: Fix palette handling with changing
    palettes
  * avcodec/raw: Fix decoding of ilacetest.mov
  * avformat/mov: Enable mp3 parsing if a packet needs it
  * avformat/hls: Sync starting segment across variants on
    live streams
  * avformat/hls: Fix regression with ranged media segments
  * avcodec/ffv1enc: Fix assertion failure with non zero
    bits per sample
  * avfilter/af_hdcd: small fix in af_hdcd.c where gain was
    not being adjusted for "attenuate slowly"
  * avformat/oggdec: Fix integer overflow with invalid pts
  * libavcodec/dnxhd: Enable 12-bit DNxHR support.
  * lavc/vaapi_encode_h26x: Fix a crash if "." is not the
    decimal separator.
  * avcodec/vp9_parser: Check the input frame sizes for
    being consistent
  * avformat/flvdec: parse keyframe before a/v stream was
    created add_keyframes_index() when stream created or
    keyframe parsed
  * libavformat/rtpdec_asf: zero initialize the AVIOContext
    struct
  * libx264: Increase x264 opts character limit to 4096
  * avcodec/h264_parser: Set sps/pps_ref
  * librtmp: Avoid an infinite loop setting connection
    arguments
  * avformat/oggparsevp8: fix pts calculation on pages
    ending with an invisible frame
  * lavf/vplayerdec: Improve auto-detection.
  * lavc/mediacodecdec_h264: properly convert extradata to
    annex-b
* Fri Jul 29 2016 jengelh@inai.de
- Build with netcdf so as to enable af_sofalizer [boo#983398]
* Fri Jul  1 2016 aloisio@gmx.com
- Update to version 3.1.1
  * doc/APIchanges: document the lavu/lavf field moves
  * avformat/avformat: Move new field to the end of AVStream
  * avformat/utils: update deprecated AVStream->codec when the context is updated
  * avutil/frame: Move new field to the end of AVFrame
  * libavcodec/exr : fix decoding piz float file.
  * avformat/mov: Check sample size
  * lavfi: Move new field to the end of AVFilterContext
  * lavfi: Move new field to the end of AVFilterLink
  * ffplay: Fix usage of private lavfi API
  * lavc/mediacodecdec_h264: add missing NAL headers to SPS/PPS buffers
  * lavc/pnm_parser: disable parsing for text based PNMs
* Mon Jun 27 2016 aloisio@gmx.com
- Update to version 3.1
  * DXVA2-accelerated HEVC Main10 decoding
  * fieldhint filter
  * loop video filter and aloop audio filter
  * Bob Weaver deinterlacing filter
  * firequalizer filter
  * datascope filter
  * bench and abench filters
  * ciescope filter
  * protocol blacklisting API
  * MediaCodec H264 decoding
  * VC-2 HQ RTP payload format (draft v1) depacketizer and
    packetizer
  * VP9 RTP payload format (draft v2) packetizer
  * AudioToolbox audio decoders
  * AudioToolbox audio encoders
  * coreimage filter (GPU based image filtering on OSX)
  * libdcadec removed
  * bitstream filter for extracting DTS core
  * ADPCM IMA DAT4 decoder
  * musx demuxer
  * aix demuxer
  * remap filter
  * hash and framehash muxers
  * colorspace filter
  * hdcd filter
  * readvitc filter
  * VAAPI-accelerated format conversion and scaling
  * libnpp/CUDA-accelerated format conversion and scaling
  * Duck TrueMotion 2.0 Real Time decoder
  * Wideband Single-bit Data (WSD) demuxer
  * VAAPI-accelerated H.264/HEVC/MJPEG encoding
  * DTS Express (LBR) decoder
  * Generic OpenMAX IL encoder with support for Raspberry Pi
  * IFF ANIM demuxer & decoder
  * Direct Stream Transfer (DST) decoder
  * loudnorm filter
  * MTAF demuxer and decoder
  * MagicYUV decoder
  * OpenExr improvements (tile data and B44/B44A support)
  * BitJazz SheerVideo decoder
  * CUDA CUVID H264/HEVC decoder
  * 10-bit depth support in native utvideo decoder
  * libutvideo wrapper removed
  * YUY2 Lossless Codec decoder
- Added minimum requirement for libva (0.35.0, matched by
  1.3.0 package)
* Tue May 31 2016 robert.munteanu@gmail.com
- Guard usage of opencore using bcond_with, boo#980542
* Thu Apr 28 2016 aloisio@gmx.com
- Update to version 3.0.2
  * avcodec/ttaenc: Reallocate packet if its too small
  * configure: build fix for P5600 with mips code restructuring
  * mips: add support for R6
  * pgssubdec: fix subpicture output colorspace and range
  * avcodec/ac3dec: Reset SPX when switching from EAC3 to AC3
  * avfilter/vf_drawtext: Check return code of load_glyph()
  * avformat/mux: Check that deinit is set before calling it
  * avcodec/takdec: add code that got somehow lost in process of
    REing
  * avcodec/apedec: fix decoding of stereo files with one
    channel full of silence
  * avcodec/avpacket: Fix off by 5 error
  * avcodec/h264: Fix for H.264 configuration parsing
  * avcodec/bmp_parser: Ensure remaining_size is not too small
    in startcode packet crossing corner case
  * avcodec/pngdec: Fix alpha detection with skip_frame
  * Changelog: Make formating consistent
  * avfilter/src_movie: fix how we check for overflows with
    seek_point
  * avcodec/j2kenc: Add attribution to OpenJPEG project:
- Dropped dcadec (libdca was merged upstream)
* Mon Apr 25 2016 jengelh@inai.de
- Add ffmpeg-codec-choice.diff
* Sun Apr 17 2016 olaf@aepfle.de
- Remove ffmpeg-devel subpackage.
  All users have been converted to pkgconfig
  Add Provides/Obsoletes to libavdevice-devel
* Sun Apr 10 2016 jengelh@inai.de
- Add ffmpeg-new-coder-errors.diff
* Wed Apr  6 2016 jengelh@inai.de
- Another try at organizing the codec-enable list.
  Enable video: AYUV, Dirac, MJPEG, rawvideo, Theora, VP8, VP9, WebP,
  zlib
  Enable audio: Celt, GSM, Opus, Speex, Vorbis
  Enable subtitle: ASS/SSA text, SRT text, UTF-8 plaintext
* Wed Mar 30 2016 jengelh@inai.de
- Update to new maintenance release 3.0.1
  * vc2enc: fix use of uninitialized variables in the rate control
  system
  * postproc: fix an unaligned access
  * lavc/hevc: Allow arbitrary garbage in bytestream as long as at
  least one NAL unit is found.
* Tue Feb 16 2016 olaf@aepfle.de
- Update included pkgconfig files to require the exact version
  of ffmpeg pc files, instead of any later version
  ffmpeg-pkgconfig-version.patch
* Mon Feb 15 2016 idonmez@suse.com
- Remove the optional vo-aacenc dependency, upstream removed it.
* Mon Feb 15 2016 jengelh@inai.de
- Update to new upstream release 3.0
  * New filters: extrastereo, ocr, alimiter, stereowiden, stereotools,
  rubberband, tremolo, agate, chromakey, displace, and many more.
  * ffplay dynamic volume control
  * audio high-order multiband parametric equalizer
  * automatic bitstream filtering
* Tue Feb  2 2016 aloisio@gmx.com
- Update to version 2.8.6
  * avcodec/jpeg2000dec: More completely check cdef
  * avutil/opt: check for and handle errors in av_opt_set_dict2()
  * avcodec/flacenc: fix calculation of bits required in case
    of custom sample rate
  * avformat: Document urls a bit
  * avformat/libquvi: Set default demuxer and protocol
    limitations
  * avformat/concat: Check protocol prefix
  * doc/demuxers: Document enable_drefs and use_absolute_path
  * avcodec/mjpegdec: Check for end for both bytes in unescaping
  * avcodec/mpegvideo_enc: Check for integer overflow in
    ff_mpv_reallocate_putbitbuffer()
  * avformat/avformat: Replace some references to filenames by
    urls
  * avcodec/wmaenc: Check ff_wma_init() for failure
  * avcodec/mpeg12enc: Move high resolution thread check to
    before initializing threads
  * avformat/img2dec: Use AVOpenCallback
  * avformat/avio: Limit url option parsing to the documented
    cases
  * avformat/img2dec: do not interpret the filename by default
    if a IO context has been opened
  * avcodec/ass_split: Fix null pointer dereference in
    ff_ass_style_get()
  * mov: Add an option to toggle dref opening
  * avcodec/gif: Fix lzw buffer size
  * avcodec/put_bits: Assert buf_ptr in flush_put_bits()
  * avcodec/tiff: Check subsample & rps values more completely
  * swscale/swscale: Add some sanity checks for srcSlice*
    parameters
  * swscale/x86/rgb2rgb_template: Fix planar2x() for short
    width
  * swscale/swscale_unscaled: Fix odd height inputs for
    bayer_to_yv12_wrapper()
  * swscale/swscale_unscaled: Fix odd height inputs for
    bayer_to_rgb24_wrapper()
  * avcodec/aacenc: Check both channels for finiteness
  * asfdec_o: check for too small size in asf_read_unknown
  * asfdec_o: break if EOF is reached after
    asf_read_packet_header
  * asfdec_o: make sure packet_size is non-zero before seeking
  * asfdec_o: prevent overflow causing seekback
  * asfdec_o: check avio_skip in asf_read_simple_index
  * asfdec_o: reject size > INT64_MAX in asf_read_unknown
  * asfdec_o: only set asf_pkt->data_size after sanity checks
  * Merge commit '8375dc1dd101d51baa430f34c0bcadfa37873896'
  * dca: fix misaligned access in avpriv_dca_convert_bitstream
  * brstm: fix missing closing brace
  * brstm: also allocate b->table in read_packet
  * brstm: make sure an ADPC chunk was read for adpcm_thp
  * vorbisdec: reject rangebits 0 with non-0 partitions
  * vorbisdec: reject channel mapping with less than two
    channels
  * ffmdec: reset packet_end in case of failure
  * avformat/ipmovie: put video decoding_map_size into packet
    and use it in decoder
  * avformat/brstm: fix overflow
* Sun Jan 17 2016 idonmez@suse.com
- Update to version 2.8.5
  * Fixes CVE-2016-1897 and CVE-2016-1898 [boo#961937]
* Mon Dec 28 2015 idonmez@suse.com
- Update to version 2.8.4
  * Many bugfixes, see the included Changelog for all the changes.
  * resolving CVE-2015-8661 [boo#960385], CVE-2015-8662 [boo#960384],
  CVE-2015-8663 [boo#960383]
- Drop ffmpeg-remove_some_unused_ctrl_id_mappings.patch, fixed
  upstream.
* Tue Dec 22 2015 olaf@aepfle.de
- Obsolete ffmpeg-tools from packman
* Mon Dec 21 2015 jengelh@inai.de
- Add some provides to make it easier for firefox to recommend
  this package for installation
* Sat Dec 19 2015 joerg.lorenzen@ki.tng.de
- Added patch ffmpeg-remove_some_unused_ctrl_id_mappings.patch to
  successfully build against libvpx >= 1.5 (at least on PMBS).
* Thu Dec 17 2015 olaf@aepfle.de
- Add buildconditionals for libass,libva,vdpau to fix build in SLE_11
* Mon Dec 14 2015 olaf@aepfle.de
- Rename bcond dca to dcadec
- Add more buildconditionals to get closer to removal of BUILD_ORIG
* Wed Dec  9 2015 olaf@aepfle.de
- Remove unused imlib2
* Mon Dec  7 2015 idonmez@suse.com
- Sync with packman changes
  * All packman specific changes are protected with BUILD_ORIG
- Added the following patches
  * ffmpeg-2.4.5-arm6l.patch
  * ffmpeg-libcdio_cdda-pkgconfig.patch
* Sun Nov 29 2015 jengelh@inai.de
- Update to new upstream maintenance release 2.8.3
  * avformat/matroskadec: Check subtitle stream before dereferencing
  * avcodec/jpeg2000dec: Fix potential integer overflow with tile
  dimensions
  * avcodec/jpeg2000dec: Check for duplicate SIZ marker
  * avcodec/jpeg2000: Change coord to 32bit to support larger than
  32k width or height
  * avcodec/jpeg2000dec: Check SIZ dimensions to be within the
  supported range
  * avcodec/jpeg2000: Check comp coords to be within the supported
  size
  * dds: validate compressed source buffer size
  * dds: validate source buffer size before copying
  * softfloat: assert when the argument of av_sqrt_sf is negative
- Fixes CVE-2015-8363 [bnc#957114], CVE-2015-8364 [bnc#957115],
  CVE-2015-8365 [bnc#957116]
* Sat Nov 14 2015 idonmez@suse.com
- Update to new upstream release 2.8.2, containing fixes for the
  following security issues:
  * CVE-2015-8216 boo#955346
  * CVE-2015-8217 boo#955347
  * CVE-2015-8218 boo#955348
  * CVE-2015-8219 boo#955350
- Upstream changes:
  * various fixes in the aac_fixed decoder
  * various fixes in softfloat
  * swresample/resample: increase precision for compensation
  * lavf/mov: add support for sidx fragment indexes
  * avformat/mxfenc: Only store user comment related tags when needed
  * ffmpeg: Don't try and write sdp info if none of the outputs had an rtp format.
  * apng: use correct size for output buffer
  * jvdec: avoid unsigned overflow in comparison
  * avcodec/jpeg2000dec: Clip all tile coordinates
  * avcodec/microdvddec: Check for string end in 'P' case
  * avcodec/dirac_parser: Fix undefined memcpy() use
  * avformat/xmv: Discard remainder of packet on error
  * avformat/xmv: factor return check out of if/else
  * avcodec/mpeg12dec: Do not call show_bits() with invalid bits
  * avcodec/faxcompr: Add missing runs check in decode_uncompressed()
  * libavutil/channel_layout: Check strtol*() for failure
  * avformat/mpegts: Only start probing data streams within probe_packets
  * avcodec/hevc_ps: Check chroma_format_idc
  * avcodec/ffv1dec: Check for 0 quant tables
  * avcodec/mjpegdec: Reinitialize IDCT on BPP changes
  * avcodec/mjpegdec: Check index in ljpeg_decode_yuv_scan() before using it
  * avcodec/h264_slice: Disable slice threads if there are multiple access units in a packet
  * avformat/hls: update cookies on setcookie response
  * opusdec: Don't run vector_fmul_scalar on zero length arrays
  * avcodec/opusdec: Fix extra samples read index
  * avcodec/ffv1: Initialize vlc_state on allocation
  * avcodec/ffv1dec: update progress in case of broken pointer chains
  * avcodec/ffv1dec: Clear slice coordinates if they are invalid or slice header decoding fails for other reasons
  * rtsp: Allow $ as interleaved packet indicator before a complete response header
  * videodsp: don't overread edges in vfix3 emu_edge.
  * avformat/mp3dec: improve junk skipping heuristic
  * concatdec: fix file_start_time calculation regression
  * avcodec: loongson optimize h264dsp idct and loop filter with mmi
  * avcodec/jpeg2000dec: Clear properties in jpeg2000_dec_cleanup() too
  * avformat/hls: add support for EXT-X-MAP
  * avformat/hls: fix segment selection regression on track changes of live streams
  * configure: Require libkvazaar < 0.7.
  * avcodec/vp8: Do not use num_coeff_partitions in thread/buffer setup
- Drop ffmpeg-mov-sidx-fragment.patch, fixed upstream.
* Sat Oct 31 2015 idonmez@suse.com
- Update to new upstream release 2.8.1
  * Minor bugfix release
  * Includes all changes from. Ffmpeg-mt,
    libav master of 2015-08-28, libav 11 as of 2015-08-28
- Add ffmpeg-mov-sidx-fragment.patch to add sidx fragment indexes.
  Needed for new mpv release.
* Wed Sep  9 2015 jengelh@inai.de
- Update to new upstream release 2.8
  * DirectDraw Surface image/texture decoder
  * Many improvements to the JPEG 2000 decoder
  * New video filters: colorkey, SSIM, showvolume, adrawgraph,
  drawgraph, removegrain, erosion, dilation, deflate, inflate,
  reverse, atadenoise, aphasemeter, showfreqs, vectorscope,
  waveform, hstack, vstack, framerate
  * New audio filters: Dynamic Audio Normalizer as dynaudnorm
  filter, areverse, random, deband, sidechaincompress,
  acrossfade
  * allyuv and allrgb video sources
  * Switched default encoders for webm to VP9 and Opus
  * Removed experimental flag from the JPEG 2000 encoder
* Mon Jul 20 2015 jengelh@inai.de
- Update to new upstream release 2.7.2
- webp: fix infinite loop in webp_decode_frame
- huffyuvdec: validate image size
- avcodec/vp8: Check buffer size in vp8_decode_frame_header()
- avcodec/vp8: Fix null pointer dereference in ff_vp8_decode_free()
- avutil/fifo: Fix the case where func() returns less bytes than
  requested in av_fifo_generic_write()
- bytestream2: set the reader to the end when reading more than
  available
- oggparsedirac: check return value of init_get_bits
- vp9/update_prob: prevent out of bounds table read
- avcodec/pngdec: Check values before updating context in
  decode_fctl_chunk()
- avcodec/pngdec: Copy IHDR & plte state from last thread
- avcodec/pngdec: Require a IHDR chunk before fctl
- avcodec/pngdec: Only allow one IHDR chunk
- ffmpeg: Do not use the data/size of a bitstream filter
  after failure
* Thu Jun 25 2015 jengelh@inai.de
- Enable codecs for audio: PCM, Speex, CELT, FLAC, ILBC, Opus
- Enable codecs for image: BMP/PCX/TGA, TIFF, Sun/SGI/X11 raster
  raw Huff-compressed or uncompressed YUV
- Update to new upstream release 2.7.1
  * postproc: fix unaligned access
  * avcodec/flacenc: Fix Invalid Rice order
  * tls_gnutls: fix hang on disconnection
  * avcodec/ffv1enc: fix bps for >8bit yuv when not explicitly set
  * avio: fix potential crashes when combining ffio_ensure_seekback + crc
  * ffmpeg_opt: Check for localtime() failure
  * configure: Disable VSX on unspecified / generic CPUs
* Thu Jun 25 2015 develop7@develop7.info
- Enabled 'bluray' protocol
* Wed Jun 10 2015 jengelh@inai.de
- Update to new upstream release 2.7
  * New encoders: apng (PNG with alpha)
  * New decoders: TDSC (a JPEG/BGR24/zlib format)
  * New audio filters: chorus
  * New video filters: cover_rect, detelecine, fftfilt, find_rect
- Enable codecs: 012v, ansi, apng, bmp, exr, ffv1, ffvhuff
  * unpack DivX-style packed B-frames in MPEG-4 bitstream filter
  * WebM Live Chunk Muxer
  * nvenc level and tier options
- Canopus HQ/HQA decoder
- Automatically rotate videos based on metadata in ffmpeg
- improved Quickdraw compatibility
- VP9 high bit-depth and extended colorspaces decoding support
- WebPAnimEncoder API when available for encoding and muxing WebP
- Direct3D11-accelerated decoding
- Support Secure Transport
- Multipart JPEG demuxer
* Sat May 23 2015 robert.munteanu@gmail.com
- Fix building with BUILD_ORIG
* Sun May 17 2015 jengelh@inai.de
- Update to new upstream release 2.6.3
  * avcodec/libtheoraenc: Check for av_malloc failure
  * ffmpeg_opt: Fix -timestamp parsing
  * avcodec/cavsdec: Use ff_set_dimensions()
  * swr: fix alignment issue caused by 8ch sse functions
  * avcodec/mjpegdec: fix len computation in ff_mjpeg_decode_dqt()
  * avformat/matroskadec: Cleanup error handling for bz2 & zlib
  * avformat/matroskaenc: Check ff_vorbiscomment_length in
  put_flac_codecpriv()
  * avcodec/mpeg12dec: use the correct dimensions for checking SAR
  * xcbgrab: Validate the capture area
  * xcbgrab: Do not assume the non shm image data is always available
  * avfilter/lavfutils: disable frame threads when decoding a single
  image
  * ffmpeg: remove incorrect network deinit
  * OpenCL: Avoid potential buffer overflow in cmdutils_opencl.c
  * libvpxenc: only set noise reduction w/vp8
  * vp9: remove another optimization branch in iadst16 which causes
  overflows.
  * network: Do not leave context locked on error
  * vp9: remove one optimization branch in iadst16 which causes
  overflows.
  * swresample: Allow reinitialization without ever setting channel
  layouts/counts
  * imgutils: initialize palette padding bytes in av_image_alloc
  * id3v2: catch avio_read errors in check_tag
  * avi: Validate sample_size
  * diracdec: avoid overflow of bytes*8 in decode_lowdelay
  * diracdec: prevent overflow in data_unit_size check
  * matroskadec: use uint64_t instead of int for index_scale
  * pngdec: don't use AV_PIX_FMT_MONOBLACK for apng
  * pngdec: return correct error code from decode_frame_common
  * swscale/ppc/swscale_altivec.c: POWER LE support in yuv2planeX_8()
  delete macro GET_VF() it was wrong
  * matroskadec: export cover art correctly
  * mxfenc: don't try to write footer without header
- Enable building avresample for extra API compat
- Remove ffmpeg-pkgconfig-requires.diff: RPM's pkgconfigdeps.sh is
  scanning Requires.private too.
* Mon May 11 2015 dimstar@opensuse.org
- Add baselibs.conf: provide -32bit libraries (used by xine-32bit).
* Mon Apr 13 2015 jengelh@inai.de
- Update to new upstream release 2.6.2
  * avformat/utils: avoid discarded streams in
  av_find_default_stream_index()
  * avutil/cpu: add missing check for mmxext to av_force_cpu_flags
  * avformat/http: replace cookies with updated values instead of
  appending forever
* Thu Mar 19 2015 jengelh@inai.de
- Update to new upstream release 2.6.1
  * Maintenance release with some bugfixes
* Sun Mar  8 2015 jengelh@inai.de
- Update to new upstream release 2.6
  * The VP9 decoder is now usable on x86(-32) and pre-SSSE3 CPUs.
  * 10-bit support in the SPP video filter
  * New video filters: "colorlevels", "tblend", "palettegen",
  "paletteuse". New audio filters: "dcshift".
  * The old libmpcodecs wrapper is finally gone
  * API changes: introduction of device inputs and outputs
* Tue Jan 27 2015 jengelh@inai.de
- Update to new upstream release 2.5.3
  * AVFoundation screen-grabbing support, animated WebP decoding
  support, and Animated PNG support. UDP-Lite support was added.
* Sun Jan  4 2015 jengelh@inai.de
- Initial package (version 2.5.3) for build.opensuse.org
