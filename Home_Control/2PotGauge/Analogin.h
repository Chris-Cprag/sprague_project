
class Analogin{
  private:
    unsigned int number;

  public:
    Analogin();
    Analogin(unsigned int n);
    virtual unsigned int getNumber() {return number;}
    virtual void setNumber(unsigned int n);
    virtual int readAdcSample();
    virtual ~Analogin();
};
