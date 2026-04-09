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
        if ( i >= 0 && i < length ) return *(p + i);
        return -1;
    }

    void set(int i, int n) {
        if ( i >= 0 && i < length ) *(p + i) = n;
    }

    void pushback(int n) {
        if (length == c) {
            this->resize();
        }
        *(p + length) = n;
        ++length;
    }

    int popback() {
        --length;
        return *(p + length);
    }

    void resize() {
        int* new_p = new int[c * 2];
        c *= 2;
        for(int i = 0; i < length; i++){
            *(new_p + i) = *(p + i);
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
