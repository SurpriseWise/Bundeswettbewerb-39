class Program
{
    public static void Main()
    {
        Console.WriteLine("Passowort wird generiert");

        string[] vokal = { "a", "e", "i", "o", "u" };
        string[] konsonant = { "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"};
        
        Random zufall = new Random();

        string silbe1 = $"{konsonant[zufall.Next(21)]}{vokal[zufall.Next(5)]}{konsonant[zufall.Next(21)]}";
        string silbe2 = $"{konsonant[zufall.Next(21)]}{vokal[zufall.Next(5)]}{konsonant[zufall.Next(21)]}";
        string silbe3 = $"{konsonant[zufall.Next(21)]}{vokal[zufall.Next(5)]}{konsonant[zufall.Next(21)]}";
        string silbe4 = $"{konsonant[zufall.Next(21)]}{vokal[zufall.Next(5)]}{konsonant[zufall.Next(21)]}";
        string silbe5 = $"{konsonant[zufall.Next(21)]}{vokal[zufall.Next(5)]}{konsonant[zufall.Next(21)]}";

        int zahl1 = zufall.Next(10);
        int zahl2 = zufall.Next(10);
        int zahl3 = zufall.Next(10);
        int zahl4 = zufall.Next(10);
        int zahl5 = zufall.Next(10);

        int laenge = zufall.Next(3);
        string passwort;


        switch (laenge)
        {
            case 0:
                passwort = $"{silbe1}{zahl1}{silbe2}{zahl2}{silbe3}";
                Console.WriteLine(passwort);
                break;

            case 1:
                passwort = $"{silbe1}{zahl1}{silbe2}{zahl2}{silbe3}{zahl3}{silbe4}{zahl4}";
                Console.WriteLine(passwort);
                break;

            case 2:
                passwort = $"{silbe1}{zahl1}{silbe2}{zahl2}{silbe3}{zahl3}{silbe4}{zahl4}{silbe5}{zahl5}";
                Console.WriteLine(passwort);
                break;

            default:
                break;
        }

    }




}
