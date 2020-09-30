FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update --fix-missing

WORKDIR ./src/

RUN apt-get -y install git \
    cmake protobuf-compiler \
    build-essential

RUN apt-get -y install libusb-1.0-0-dev
RUN apt-get -y install ibglib2.0-dev
#fixes issue with installing pycurl
RUN apt-get install -y libcurl4-openssl-dev libssl-dev
#RUN pip3 install tensorflow==1.14

WORKDIR /home
RUN git clone git://git.osmocom.org/rtl-sdr.git
RUN cd rtl-sdr/
RUN mkdir build
RUN cd build
RUN cmake ./rtl-sdr/ -DINSTALL_UDEV_RULES=ON -DDETACH_KERNEL_DRIVER=ON
RUN make
RUN make install
RUN ldconfig

#RUN mkdir classifier
#copy these into image
#COPY /libusb-1.0.dll /home/classifier
#COPY /rtlsdr.dll /home/classifier

RUN apt-get -y install python3.7 \
    python3-pip

RUN pip3 install tensorflow==1.14

RUN pip3 install asgiref==1.1.2 \
    astroid==1.5.3 \
    astropy==2.0.2 \
    attrs==17.3.0 \
    autobahn==17.10.1 \
    Automat==0.6.0 \
    babel==2.5.0 \
    backports.shutil-get-terminal-size==1.0.0 \
    beautifulsoup4==4.6.0 \
    bitarray==0.8.1 \
    bkcharts==0.2 \
    blaze==0.10 \
    bleach==3.1.4 \
    bokeh==0.12.7 \
    boto==2.48.0 \
    Bottleneck==1.2.1

RUN pip3 install CacheControl==0.12.3 \
    certifi==2017.7.27.1 \
    cffi==1.10.0 \
    chardet==3.0.4 \
    click==6.7 \
    cloudpickle==0.4.0 \
    clyent==1.2.1 \
    colorama==0.3.9 \
    comtypes==1.1.7 \
    conda==4.3.16 \
    constantly==15.1.0 \
    contextlib2==0.5.5 \
    cycler==0.10.0 \
    Cython==0.26.1 \
    cytoolz==0.8.2 \
    dask==0.15.2 \
    datashape==0.5.2 \
    decorator==4.1.2 \
    distlib==0.2.5 \
    distributed==1.18.3 \
    docutils==0.14

RUN pip3 install entrypoints==0.2.3 \
    enum34==1.1.6 \
    et-xmlfile==1.0.1 \
    fastcache==1.0.2 \
    filelock==2.0.12 \
    future==0.16.0 \
    gevent==1.2.2 \
    glob2==0.5 \
    greenlet==0.4.12 \
    h5py==2.7.0 \
    heapdict==1.0.0 \
    html5lib==0.9999999 \
    hyperlink==17.3.1 \
    idna==2.6 \
    imageio==2.2.0 \
    imagesize==0.7.1 \
    incremental==17.5.0 \
    ipykernel==4.6.1 \
    ipython==6.1.0 \
    ipython-genutils==0.2.0 \
    ipywidgets==7.0.0 \
    isort==4.2.15 \
    itsdangerous==0.24 \
    jdcal==1.3 \
    jedi==0.10.2 \
    jsondatabase==0.1.7 \
    jsonschema==2.6.0 \
    Keras==2.1.1 \
    lazy-object-proxy==1.3.1 \
    llvmlite==0.20.0 \
    locket==0.2.0 \
    lockfile==0.12.2 \
    lxml==3.8.0

RUN pip3 install Markdown==2.6.9 \
    MarkupSafe \
    mathparse==0.1.1 \
    matplotlib==2.0.2 \
    mccabe==0.6.1 \
    mpmath==0.19 \
    msgpack-python==0.4.8 \
    multipledispatch==0.4.9 \
    nbconvert==5.3.1 \
    nbformat==4.4.0 \
    networkx==1.11 \
    nltk==3.4.5 \
    nose==1.3.7 \
    numba==0.35.0 \
    numexpr==2.6.2 \
    numpy \
    numpydoc==0.7.0 \
    oauthlib==2.0.6 \
    odo==0.5.0 \
    olefile==0.44

RUN pip3 install packaging==16.8 \
    pandas==0.21.1 \
    pandocfilters==1.4.2 \
    partd==0.3.8 \
    path.py==10.3.1 \
    pathlib2==2.3.0 \
    patsy==0.4.1 \
    pep8==1.7.0 \
    pickleshare==0.7.4 \
    Pillow==6.2.0 \
    pkginfo==1.4.1 \
    ply==3.10 \
    progress==1.3 \
    prompt-toolkit==1.0.15 \
    protobuf==3.4.0 \
    psutil==5.6.6 \
    py==1.4.34 \
    pycodestyle==2.3.1 \
    pycosat==0.6.3 \
    pycparser==2.18 \
    pycurl==7.43.0 \
    pyflakes==1.5.0 \
    pygame==1.9.3 \
    Pygments==2.2.0 \
    pylint==1.7.2 \
    pymongo==3.5.1 \
    pyparsing==2.2.0 \
    pyrtlsdr==0.2.7 \
    pyserial==3.4 \
    PySocks==1.6.7 \
    pytest==3.2.1 \
    python-dateutil==2.6.1 \
    pytz==2017.2 \
    PyWavelets==0.5.2 \
    pyzmq==16.0.2 \
    ruamel.yaml==0.15.0

RUN pip3 install scikit-image==0.13.0 \
    scikit-learn==0.21.3 \
    scipy==1.1.0 \
    seaborn==0.8 \
    simplegeneric==0.8.1 \
    singledispatch==3.4.0.3 \
    six==1.11.0 \
    snowballstemmer==1.2.1 \
    sortedcollections==0.5.3 \
    sortedcontainers==1.5.7 \
    spyder==3.2.3 \
    statsmodels==0.8.0 \
    sympy==1.1.1 \
    tables==3.4.2 \
    tblib==1.3.2 \
    testpath==0.3.1 \
    tflearn==0.3.2 \
    Theano==1.0.0 \
    toolz==0.8.2 \
    tornado==4.5.2 \
    tqdm==4.19.4 \
    traitlets==4.3.2 \
    txaio==2.8.2 \
    typing==3.6.2

RUN pip3 install unicodecsv==0.14.1 \
    visvis==1.10.0 \
    wcwidth==0.1.7 \
    webencodings==0.5.1 \
    widgetsnbextension==3.0.2 \
    wrapt==1.10.11 \
    xlrd==1.1.0 \
    xlwt==1.3.0 \
    zict==0.1.2 \
    zope.interface==4.4.3

#solves an issue with protobuf
RUN pip3 install -U protobuf

RUN apt-get install -y wget
RUN apt-get install -y pkg-config zip g++ zlib1g-dev unzip python
RUN wget https://github.com/bazelbuild/bazel/releases/download/0.22.0/bazel-0.22.0-installer-linux-x86_64.sh
RUN chmod u+x bazel-0.22.0-installer-linux-x86_64.sh
RUN ./bazel-0.22.0-installer-linux-x86_64.sh --user

WORKDIR /home/classifier

#For quickly grabbing original source code
RUN git clone https://github.com/marcella-benner/cnn-kerbossdr

WORKDIR /home/classifier/cnn-kerberossdr

#For automatically executing scripts upon startup
ENTRYPOINT ["python3"]
CMD ["prepare.py"]

#CMD /bin/bash