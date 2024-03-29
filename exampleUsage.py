from BuildVuClient import BuildVu

buildvu = BuildVu('http://localhost:8080/microservice-example')

try:
    # Upload a local file to the BuildVu microservice
    # convert() returns an dictionary with the conversion results.
    conversionResults = buildvu.convert(input=BuildVu.UPLOAD, file='path/to/file.pdf')

    # You can specify other parameters for the API as named parameters, for example
    # here is the use of the callbackUrl parameter which is a URL that you want to 
    # be updated when the conversion finishes. 
    # See https://github.com/idrsolutions/buildvu-microservice-example/blob/master/API.md
    #conversionResults = buildvu.convert(input=BuildVu.UPLOAD,
    #                            callbackUrl='http://listener.url')

    # Alternatively, you can specify a url from which the server will download the file to convert.
    #conversionResults = buildvu.convert(url='http://link.to/filename',
    #                            input=BuildVu.DOWNLOAD)

    outputURL = conversionResults['downloadUrl']

    # After the conversion you can also specify a directory to download the output to:
    #buildvu.downloadResult(conversionResults, 'path/to/output/dir')

    if outputURL is not None:
        print("Converted: " + outputURL)
except Exception as error:
    print(error)
