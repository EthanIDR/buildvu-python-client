from BuildVuClient import BuildVu

buildvu = BuildVu('http://localhost:8080/microservice-example')

try:
    # convert() returns a URL (string) where you can view the converted output.
    outputURL = buildvu.convert("path/to/file.pdf")
    # OR for sending via url:
    #outputURL = buildvu.convert("http://example/url/file.pdf", isUrl=True)

    if outputURL is not None:
        print("Converted: " + outputURL)

    # You can also specify a directory to download the converted output to:
    # buildvu.convert('path/to/input.pdf', 'path/to/output/dir')
except Exception as error:
    print(error)
