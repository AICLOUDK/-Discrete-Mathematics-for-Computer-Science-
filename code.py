# In[1]:


import sys, threading


sys.setrecursionlimit(10**7)
threading.stack_size(2**27)


def ConvertToInt(message_str):
  res = 0
  for i in range(len(message_str)):
    res = res * 256 + ord(message_str[i])
  return res

def ConvertToStr(n):
    res = ""
    while n > 0:
        res += chr(n % 256)
        n //= 256
    return res[::-1]

def PowMod(a, n, mod):
    if n == 0:
        return 1 % mod
    elif n == 1:
        return a % mod
    else:
        b = PowMod(a, n // 2, mod)
        b = b * b % mod
        if n % 2 == 0:
          return b
        else:
          return b * a % mod

def ExtendedEuclid(a, b):
    if b == 0:
        return (1, 0)
    (x, y) = ExtendedEuclid(b, a % b)
    k = a // b
    return (y, x - k * y)

def InvertModulo(a, n):
    (b, x) = ExtendedEuclid(a, n)
    if b < 0:
        b = (b % n + n) % n
    return b

def Decrypt(ciphertext, p, q, exponent):
  # Substitute this implementation with your code from question 2 of the "RSA Quiz".
    d = InvertModulo(exponent, (p-1)*(q-1))
    return ConvertToStr(PowMod(ciphertext, d, p * q))

p = 779849711281
q = 748173698927
e = 1018651
ciphertext = 148784435264686331994392
decrypt_first_puzzle = Decrypt(ciphertext, p, q, e)
print(decrypt_first_puzzle)

The second puzzle is based on the questions 1 and 3 of the "RSA Quiz". Here, you need to substitute our implementation of the function "Encrypt" with your implementation from question 1 and substitute our implementation of the function "DecipherSimple" with your implementation from the question 3 of the "RSA Quiz" to get the second part of the secret link.
# In[2]:


def Encrypt(message, modulo, exponent):
    # Substitute this implementation with your code from question 1 of the "RSA Quiz".
    return PowMod(ConvertToInt(message), exponent, modulo)

def DecipherSimple(ciphertext, modulo, exponent, potential_messages):
    # Substitute this implementation with your code from question 3 of the "RSA Quiz".
    for potential_message in potential_messages:
        if ciphertext == Encrypt(potential_message, modulo, exponent):
            return potential_message
    return "don't know"
ciphertext = 336184023047118677086739
modulo = 1110014195838866450995043
exponent = 767549
potential_messages = ["http://goo.gl/", "http://tinyurl.com/", "http://bit.ly/", "http://t.co/", "http://ow.ly/", "https://is.gd/", "https://buff.ly/", "http://adf.ly/", "http://bit.do/"]
decrypt_second_puzzle = DecipherSimple(ciphertext, modulo, exponent, potential_messages)
print decrypt_second_puzzle

Now you're ready to construct the secret link. Just run the next part of the notebook to get it. Then follow the link to get more instructions. Also, if you follow the correct link, you will already get the answer to the first question of the following "RSA Quest Quiz"!
# In[3]:


secret_link = decrypt_second_puzzle + decrypt_first_puzzle
print(secret_link)

Substitute the implementation of the function "DecipherSmallPrime" below with your implementation from "RSA Quiz", question 4. Also, insert the values for the ciphertext, modulo and exponent from the secret document. Then launch to get the first part of the next secret link.
# In[4]:


def DecipherSmallPrime(ciphertext, modulo, exponent):  
    for p in range(3, 1000000):
        if modulo % p == 0:
            small_prime = p
            big_prime = modulo // p
            return Decrypt(ciphertext, small_prime, big_prime, exponent)
    return "do not know"

ciphertext = 2275574988111277110437311214647848935000427550724521671610776681372035260669927879546598212402059626568529572296378786125308417822064565716822176055495534704248368924219660507214955218285229437531331022539446136060045737304497347919927268903882567968402406701512120140117419155759639779776379512631504909857
modulo = 4517997441484302732739462818197633745340869919448215356148620255867108411028738486895653782573554891335084161684285442351914740415677262295900238601126392055761648706990593425725625329173683080677363007706828763867611649178136159927562319810830366004181626803874119100160889961902072311468445073289996506931
exponent = 1927740953777951565602110467665746890410015037617105427402060961409149865403375973001399584612131360178672080227818127622463053259278787951537329431243
decrypt_third_puzzle = DecipherSmallPrime(ciphertext, modulo, exponent)
print(decrypt_third_puzzle)

Substitute the implementation of the function "DecipherSmallDiff" below with your implementation from "RSA Quiz", question 5. Also, insert the values for the ciphertext, modulo and exponent from the secret document. Then launch to get the second part of the next secret link.
# In[5]:


def IntSqrt(n):
    low = 1
    high = n
    iterations = 0
    while low < high and iterations < 5000:
        iterations += 1
        mid = (low + high + 1) // 2
        if mid * mid <= n:
            low = mid
        else:
            high = mid - 1
    return low

def DecipherSmallDiff(ciphertext, modulo, exponent):  
    for p in range(IntSqrt(modulo) - 5000, IntSqrt(modulo) + 1):
        if modulo % p == 0:
            small_prime = p
            big_prime = modulo // p
            return Decrypt(ciphertext, small_prime, big_prime, exponent)

ciphertext = 17250119573232938159495151836907345788113398812430175654066191733201327934519622049877939234487323106446778939262441322441499883118016470240906983286600405405975275723333283015774857915215814576298063848917112178624770247286048114974808099004729887688547429197942578127510912101233759373809217128865040107305284699411659572170044538767976158851028945020639377891878532187396172245359826784724912031113990729909962190626715090093246089745719249482899605241682396631713155172212615370473237731019162671529937751370463768746592055682933647328743947355593762481102849672215738899019205704001633289554719966
modulo = 51719336593283668370261446912126485319255258778617224708410520647959236475322767644636584229070380964088870777607922268179572997129414217601241230215567764098337343256793524076040868978141016236299799031426456716364496058717536559180352016088612210860181989844954906788705998058534134464446292058222426189127398972577715363401457729737792004774929189832678271680193791993183578966529414824171500027009334274604018078392873654591487139190491950796770048687394408709037045383279375259210879772320878973829171531428762995383292175994184457145115155299673171196041635346062296031613203020122378411630001719
exponent = 2370692877507893030572035746060036014373915956107619689350920177346027898716147057536168003507966056257828756067470679338655825857154534154205294932307
decrypt_fourth_puzzle = DecipherSmallDiff(ciphertext, modulo, exponent)
print(decrypt_fourth_puzzle)

Now you have both parts of the second link. To get the link, just launch the next part of the notebook. Then follow the link to get more instructions. Also, if you follow the correct link, you will get the answer to the second question of the following "RSA Quest Quiz"!
# In[6]:


second_secret_link = decrypt_third_puzzle + decrypt_fourth_puzzle
print(second_secret_link)

Substitute the implementation of the function "DecipherCommonDivisor" below with your implementation from "RSA Quiz", question 6. Also, insert the corresponding values for the ciphertexts, modulos and exponents from the second secret document. Then launch to get the first and the second parts of the final answer.
# In[7]:


def GCD(a, b):
  if b == 0:
    return a
  return GCD(b, a % b)

def DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent):
    common_prime = GCD(first_modulo, second_modulo)
    q1 = first_modulo // common_prime
    q2 = second_modulo // common_prime
    return (Decrypt(first_ciphertext, common_prime, q1, first_exponent), Decrypt(second_ciphertext, common_prime, q2, second_exponent))

first_ciphertext = 23402197839825692972957660045778005842149570897525565884030609841447497251897989699441878864356827076382914144503306327825195586612359555424774490982037582237066994974597680950158893991141848342087005739774563510316219462834998856466395854239468748012474813939969736279381474141408975441930226654470509840545902057273419529586319420996953635246047632517133343837614016964611767487664771097138242956384358875235954455242525595951902976992404807998173614628224868047333599482826829214633744976147539512358779840250950906473302037621404671062661398282452008807449216135596254412709706306612180825630285207
first_modulo = 58430823052528382232133162302686450950325469505875659240893229402912849840784309398807910065914827693927654379087691699343872463431863820528404206238621375034134223224550898236635277014485802812169842923892545064506382750914506131733421755620169771252068722149093463194110389888198706547399113274669324939230289590384817282220066815621515694361776987606124224166139632882923972455465687163365892873407377154186582920232983732264041961425519725867802358413817383859468852644174951734478657652205963797131615641353571742901542970047092056441684257125633460892715564219695534982132772847099500990153159493
first_exponent = 2746118316073165006639038412489080229254239843347153634155286882078957003180280976570735902213132927273096496684341374829942796710900231180504644399747
second_ciphertext = 30727040453983198346085853479092007121170298341280644429200282752975717255888449508484551605881216103173708171060447929559225510082705090077245435032226394315334065553706481613913603534470394670437184947722155153114209268193235042140736923023590768685692783514873340402355775735846109759697748120233777810481952073715032877304902097750445981869076182666622029473694669920172468716779937348673868171294362620903115903645873289564367176851434972937848591902468604400091051094342304122317377572964272370825515688006084797380707045470951321039467067019460709497651682710286878824565888446939229639383746
second_modulo = 42955660491543430460148980223483714568674234383080724206879432109744068992302351872678094322626198782875395264399683702531442650135501135314224418412956329257244753538669224867463416933578848236691757751760346388773871177654731330626106150400017398309330888903195999995955385444097920846918948184509773583149893677181571427932535786503554494314244294387551141996689565647925375574586590998569956897670722964200467030891957754959187718494336504559943885199686487499306417596091732019643533054349876912582987170110689841980733691588287144182824378328622431439004258091442919814253322774125364502939460173
second_exponent = 1696307946163562648509752484630349193234799326977939859599277182356207670242676510190455023892125378267322231053560789876259990406520567562708111385869
decrypt_sixth_puzzle = DecipherCommonDivisor(first_ciphertext, first_modulo, first_exponent, second_ciphertext, second_modulo, second_exponent)
print(decrypt_sixth_puzzle)

Substitute the implementation of the function "DecipherHastad" below with your implementation from "RSA Quiz", question 7. Also, insert the values for the ciphertexts and modulos from the second secret document. Then launch to get the third - and the last - part of the final answer.
# In[8]:


def ChineseRemainderTheorem(n1, r1, n2, r2):
  (x, y) = ExtendedEuclid(n1, n2)
  return ((r2 * x * n1 + r1 * y * n2) % (n1 * n2) + (n1 * n2)) % (n1 * n2)

def DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo):
  # Substitute this implementation with your code from question 7 of the "RSA Quiz".
  r = ChineseRemainderTheorem(first_modulo, first_ciphertext, second_modulo, second_ciphertext)
  return ConvertToStr(IntSqrt(r))

first_ciphertext = 1695925818934701958536732606471007147871697773728881305981426383004125888187531096540654444788889942827682032651915812560
first_modulo = 2019703097262944143745237345710626601616589344196612447233041278945420303895066774752152001687355425741826173570952817341
second_ciphertext = 438180481071044087096048173519586369091293503891810459558098521655659500752405553498472135529822589328291372879622802017
second_modulo = 968914506353797853274340817936111164236562754898105214422095149641604042531040243209810736059746240506447210425767208577

decrypt_seventh_puzzle = DecipherHastad(first_ciphertext, first_modulo, second_ciphertext, second_modulo)
print(decrypt_seventh_puzzle)

Now just launch the next part to get the final answer, then copy and paste to submit it as the answer to the question 3 of the "RSA Quest Quiz"!
# In[9]:


final_answer = decrypt_sixth_puzzle[0] + decrypt_sixth_puzzle[1] + decrypt_seventh_puzzle
print(final_answer)

