SOURCES += deps/python-poster
SOURCES += icon.png
SOURCES += main.py
SOURCES += metadata.xml

ZIP = current.zip

all: $(ZIP)

$(ZIP): $(SOURCES)
	zip -r $@ $^