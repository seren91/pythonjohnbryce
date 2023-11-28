
for( let j = 1; j <= 100; j++ )
{   
    str = '';       
    
    if( j%3 == 0 )
    {
        str += 'Fizz';
    } 

    if( j%5 == 0 )
    {
        str += 'Buzz';
    }   

    
    console.log( str ? str : j );
}



for( let j = 1; j <= 20; j++ )
{   
    str = ''; 
    console.log( str ? str : j );
}