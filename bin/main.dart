import 'dart:io';

void main(List<String> args) {
  print('ASCII Art Generator (Dart version)');
  if (args.isEmpty) {
    print('Usage: dart run bin/main.dart <image_path>');
    exit(1);
  }
}
