import java.util.Arrays;


class Test{

	// main method
	public static void main(String []args) {

		if(args.length >= 1){
			System.out.println(Arrays.toString(args));	
		}
		
		Object t = new Person("shihongguang", 27);

		Person p = (Person)t;
		p.who();
		System.out.println("\n");	
		System.out.println("class:");	
		System.out.println(p);	

    }

}
		

interface printf{
	public void print(String []args);
}

interface showf{
	public void show(String []args);
}


class Base{
	// ClassLoader test
	static {
		System.out.println("------Base------\n\n");
	}
	
	public String toString(){
		// Class
		Class c = this.getClass();	
		String str = "<%s: %s> \n-%s\n";
		return String.format(str, c.getName(), Arrays.toString(c.getConstructors()), Arrays.toString(c.getInterfaces()));
	}	
}


class Person extends Base implements printf, showf{
	// private attr can't be visited by "class.attr", but public attr.

	// class(static) attrs
	private static String _Country;
	public static String _City;
	
	// instance attrs
	public String _Name;
	public int _Age;

	// constructors
	public Person(String name, int age){
		_Name = name;
		_Age = age;
	}

	public Person(String name, int age, String city){
		_Name = name;
		_Age = age;
		_City = city;
	}

	// methods
	public void who(){
		if (_City == null || _City.length() == 0){
			System.out.println("\nset default public class attr city is beijing\n");		
			_City = "beijing";
		}
		String str = "my name is %s, I\'m %d, in %s!";
		System.out.println(String.format(str, _Name,  _Age, _City));	
	}

	// interface implements
	public void print(String []argsList){
		System.out.println(Arrays.toString(argsList));	
	}

	public void show(String []argsList){
		System.out.println(Arrays.toString(argsList));	
	}
}

