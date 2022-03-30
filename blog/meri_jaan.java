class car{
String car_model;
String car_type;
double car_price;
String insurance_type;
public void car(String car_model,String car_type,double car_type,String,insurance_type)
{
    this.car_model=car_model;
    this.car_type=car_type;
    this.car_price=car_price;
    this.insurance_type=insurance_type;
}
public static void main(String args[])
{
ArrayList<car>cars=new ArrayList<>();
Scanner sc=new Scanner(System.in);
char y='y';
    while(y=='y'||y=='Y')
    {
    String car_model;
    String car_type;
    double car_price;
    int optn;
    String insurance_type;
    System.out.println('Enter car model');
    car_model=sc.nextLine();
    System.out.println("Enter car price");
    car_price=sc.nextDoule();
    System.out.println("press 1: sedan 2:suv 3:he");
    optn=sc.nextInt();
    switch(optn){
    case 1:car_type="sedan";car_price=car_price*(8/car_price*100)break;
    case 2:car_type="Suv";car_price=car_price*(10/car_price*100)break;
    case 3:car_type="Colgate";car_price=car_price*(10/car_price*100)break;
    }
    System.out.println("select incurence type 1:primuim 2:basics");
    optn=sc.nextInt();
    switch(optn){
    case 1:insurance_type='priumum';car_price=car_price*(20/car_price*100)break;
    case 2:insurance_type='basic';car_price=car_price*(10/car_price*100)break;
    }
    System.out.println('want to add more car press y');
    y=sc.nextLine().charAt(0);
    }
}
}