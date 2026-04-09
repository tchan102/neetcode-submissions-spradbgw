class DynamicArray {
private:
int* p;
int c;
int length;
public:

    DynamicArray(int capacity) : c(capacity), length(0){
        p = new int[capacity];
    }

    ~DynamicArray(){
        delete[] p;
    }

    int get(int i) {
        return p[i];
    }

    void set(int i, int n) {
        p[i] = n;
    }

    void pushback(int n) {
        if (length == c) {
            resize();
        }
        p[length] = n;
        ++length;
    }

    int popback() {
        if(length > 0) --length;
        return p[length];
    }

    void resize() {
        c *= 2;
        int* new_p = new int[c];
        for(int i = 0; i < length; i++){
            new_p[i] = p[i];
        }
        delete []p;
        p = new_p;
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return c;
    }
};
