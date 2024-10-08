#! /usr/bin/env python3

import argparse
import os
import sys
import zlib

from typing import Optional

class File:

    MAGIC_NUMBER = b"ABJR"
    HEADER_SIZE = 16
    GZIP_SIGNATURE = b"\x1F\x8B\x08"

    def __init__(
        self,
        name,
        content,
        compression=None,
        gzip_signature_position=None,
        content_range=None
    ):
        self.name = name
        self.content = content
        self.compression = compression
        self.gzip_signature_position = gzip_signature_position
        self.content_range = content_range


    def extract_content(self) -> bytes:
        """
        Function which extracts the content from a file.
        """
        if self.compression == "gzip":
            return self._decompress_data()
        return self._extract_binary_data()


    def _extract_binary_data(self) -> bytes:
        """
        Function which extracts the binary data from a file.
        """
        start, finish = self.content_range
        return self.content[start : finish]


    def _decompress_data(self) -> Optional[bytes]:
        """
        Function which decompresses gzip data from a file.
        """
        try:
            content_start, content_finish = self.content_range
            data = self.content[self.gzip_signature_position:content_finish]
            return zlib.decompress(data, zlib.MAX_WBITS | File.HEADER_SIZE)
        except Exception as e:
            print(f"{self.name}: {e}")
            return None


    def validate_file_name(self) -> str:
        """
        Function which validates file names.
        """
        if self.name.endswith(".zbb"):
            return f"{self.name[:-4]}.bb"
        if self.name == 'bcert.pkg':
            return f"{self.name}.xml"
        if self.name == 'file.pkg':
            return f"{self.name}.txt"
        return self.name


def open_file(path) -> bytes:
    """
    Function which opens a specified file and returns the contents.
    """
    with open(path, "rb") as f:
        return f.read()


def parse_files(contents) -> list[File]:
    """
    Function which reads through the `.ahs` archive and parses file objects.
    """

    files = []
    position = 0
    while position < len(contents):

        # Search for the first instance of the magic number,
        # and set the position.
        position = contents.find(File.MAGIC_NUMBER, position)
        if position == -1:
            break

        # Set the start position of the file.
        file_start = position

        # Set the position past the magic number and default header size.
        # This includes the header flags, etc.
        position += len(File.MAGIC_NUMBER)
        position += File.HEADER_SIZE

        # Parse the name of the file.
        file_name_bytes = []
        while contents[position] != 0:
            file_name_bytes.append(contents[position])
            position += 1
        position += 1
        name = bytes(file_name_bytes).decode("utf-8")

        # Declare the finish position of the current file.
        next_magic = contents.find(File.MAGIC_NUMBER, position)
        if next_magic == -1:
            next_magic = len(contents)

        # Check if there's a gzip signature in the header,
        # and set the compression.
        gzip_signature_position = contents.find(
            File.GZIP_SIGNATURE,
            position,
            next_magic
        )
        compression = "gzip" if gzip_signature_position != -1 and gzip_signature_position < next_magic else None

        # Set the range of the file contents.
        content_range = (
            file_start + File.HEADER_SIZE + 100, next_magic
        )

        # Set the `File` object's properties and store to `files`.
        file_object = File(
            name=name,
            content=contents,
            compression=compression,
            gzip_signature_position=gzip_signature_position if compression == "gzip" else None,
            content_range=content_range
        )
        files.append(file_object)

        # Move the position to the next file.
        position = next_magic

    return files


def write_file(file_object: File, destination: str) -> None:
    """
    Function which writes data to a file.
    """

    content = file_object.extract_content()
    if content:
        output_filename = file_object.validate_file_name()
        output_path = os.path.join(destination[:-4], output_filename)
        os.makedirs(destination[:-4], exist_ok=True)
        with open(output_path, "wb") as output_file:
            output_file.write(content)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description=(
        """
        Lightweight file analysis and extraction tool for
        HPE's Active Health System (.AHS) files.
        """
        )
    )
    parser.add_argument(
        "source",
        help="specify the source file (.AHS) for analysis."
    )
    parser.add_argument(
        "--extract",
        action="store_true",
        dest="extract",
        required=False,
        help="extract all files from a .ahs source file."
    )
    arguments = parser.parse_args()

    if arguments.source and arguments.source.endswith(".ahs"):
        content = open_file(arguments.source)
        files = parse_files(content)

        if arguments.extract:
            destination = arguments.source
            for f in files:
                write_file(f, destination)

    else:
        sys.exit("Please specify a .ahs file.")
