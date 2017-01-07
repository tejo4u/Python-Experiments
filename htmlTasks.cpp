#include <iostream>
#include <string>
#include <stack>
#include <fstream>
#include <sys/stat.h>

//Basic Html File Handlings can be done better by using Regular Expressions
//Does not support all the tags! Basic tag Support is available

class htmlTasks {
private:
std::stack<std::string>tagStack;
public:

long int size(std::string filename){
      struct stat stat_buf;
      int rc = stat(filename.c_str(),&stat_buf);
      return rc == 0 ? stat_buf.st_size : -1;
  }

  std::string tagLister(char const *filename){
    if (size(filename) == 0) {
      return "Empty File! Nothing to traverse!";
    }
  std::fstream html_file_object;
  html_file_object.open(filename,std::ios::in | std::ios::out | std::ios::binary | std::ios::app );  //Open the Html file
  char ch; //Character to traverse
  std::fstream fileParser(filename, std::fstream::in);
  while (fileParser >> std::noskipws >> ch) {
      if (ch == '<') { //Encountered tag
        std::string indiTag;
        while (ch != '>') {
          indiTag.push_back(ch);
          fileParser >> std::noskipws >> ch;
        }
        indiTag.push_back('>'); // Push the last angle ' > ' bracket into string
        std::cout << indiTag << '\n';
      }
  } //End of File Traversal
  return "Successfully Scanned!";
} //End of Tag Lister

std::string tagValidator(char const *filename){
  std::fstream html_file_object;
  html_file_object.open(filename,std::ios::in | std::ios::out | std::ios::binary | std::ios::app );  //Open the Html file
  char ch;
  std::string indiTag; //Character to traverses
  std::fstream fileParser(filename, std::fstream::in);
  while (fileParser >> std::noskipws >> ch) {
      if (ch == '<') { //Encountered tag
        indiTag.clear();
        while (ch != '>') {
          indiTag.push_back(ch);
          fileParser >> std::noskipws >> ch;
          if (ch == '<') {
            return "tagging Error! Tags Inconsistent!";
          }
        }

        indiTag.push_back('>'); // Push the last angle bracket into string

        if (tagStack.size() > 0 && indiTag[1]=='/') { //Closing Tag Condition

          indiTag.erase(indiTag.find('/'),1);
          indiTag.pop_back();

          if((tagStack.top()).find(indiTag)!=std::string::npos){
            tagStack.pop(); //Consistent tag pair
          }
          else{
            return "tagging Error! Tags Inconsistent!";
          }
        }
        else
        {
         tagStack.push(indiTag);
       }
     } //End of Tag Parser condition
  } //End of File Traversal
    if (tagStack.size() > 0) {
      return "tagging Error! Tags Inconsistent!";
    }
    return "Perfect Tagging!";
} //End of Tag Validator

};
int main(int argc, char const *argv[]) {
  htmlTasks object;
  object.tagLister(argv[1]);
  std::cout << object.size(argv[1])<<" Bytes." << '\n';
  std::cout << object.tagValidator(argv[1])<< '\n';
  return 0;
}
