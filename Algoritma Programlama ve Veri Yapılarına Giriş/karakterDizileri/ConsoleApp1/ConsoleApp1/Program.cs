internal class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");

        int sayi = 2;

        Console.WriteLine(sayi); //2
        Console.WriteLine(sayi + 2); //4
                                     // açıklama ifadesi Console.WriteLine(sayi*sayi);
                                     //açıklama notları Console.WriteLine(sayi-5);
        /* Bu şekilde de yorum satırı yapabilirsin */

        //Kaçış ifadeleri

        string ifade = "C:\\user\\zcomrt";
        Console.WriteLine(ifade);
        // \n yeni satirda baslar.
        // \t tab yapar.
        //n \a ses cikarip uyari verir.
        // eger dosya yolu gibi işlemlerde \ kullanacaksan iki kere kullanip yazmalisin ornek: "C:\\user\\zcomrt"
        // veya basina @ koymalisin.



        Console.ReadKey();
    }
}