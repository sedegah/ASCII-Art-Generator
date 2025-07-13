// File: bin/main.dart
import 'dart:io';
import 'package:image/image.dart' as img;

const charsets = {
  'dense': '@%#*+=-:. ',
  'sparse': '#O+=- ',
  'binary': '10'
};

String getAsciiChar(int gray, String charset) {
  final scale = charset.length;
  return charset[(gray / 255 * (scale - 1)).floor()];
}

String imageToAscii(String path, {int width = 100, String charset = 'dense'}) {
  final bytes = File(path).readAsBytesSync();
  final image = img.decodeImage(bytes);
  if (image == null) throw Exception('Unable to load image.');

  final aspectRatio = image.height / image.width;
  final height = (aspectRatio * width * 0.55).round();
  final resized = img.copyResize(image, width: width, height: height);

  final buffer = StringBuffer();
  for (int y = 0; y < resized.height; y++) {
    for (int x = 0; x < resized.width; x++) {
      final pixel = resized.getPixel(x, y);
      final r = img.getRed(pixel);
      final g = img.getGreen(pixel);
      final b = img.getBlue(pixel);
      final gray = ((r + g + b) / 3).round();
      buffer.write(getAsciiChar(gray, charsets[charset]!));
    }
    buffer.writeln();
  }
  return buffer.toString();
}

void main(List<String> args) {
  if (args.isEmpty) {
    print('Usage: dart run bin/main.dart <image_path> [--width=100] [--charset=dense]');
    exit(1);
  }

  final path = args[0];
  final widthArg = args.firstWhere((arg) => arg.startsWith('--width='), orElse: () => '--width=100');
  final charsetArg = args.firstWhere((arg) => arg.startsWith('--charset='), orElse: () => '--charset=dense');

  final width = int.tryParse(widthArg.split('=')[1]) ?? 100;
  final charset = charsetArg.split('=')[1];

  if (!charsets.containsKey(charset)) {
    print('Invalid charset. Use: dense, sparse, or binary.');
    exit(1);
  }

  try {
    final ascii = imageToAscii(path, width: width, charset: charset);
    print(ascii);
  } catch (e) {
    print('Error: \$e');
    exit(1);
  }
}
