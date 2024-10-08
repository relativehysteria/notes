non-exhaustive guidelines pro programování v C. tenhle dokument byl specificky
sepsaný pro kulišáky na vutbr a zmiňuje jenom non-negotiable věci -- žádný
specifický howto na psaní dobrého a bezpečného kódu (mimo základy).

## Formatting

### 1. Headers and Header Files

Každý `.c` a `.h` soubor musí mít header koment, ve kterém je v angličtině zmíněn
* Popis IFJ projektu (`// Project: Implementation of a compiler for the IFJ24 imperative language.`)
* Zodpovědný autor.
* Popis souboru (například `Procedures and structs for working with expression stacks.`)

Každý `.h` soubor musí obsahovat guard ve formě
[`#pragma once`](https://en.wikipedia.org/wiki/Pragma_once). Tenhle guard
uváďějte _pod_ header koment. Nepoužívejte starý `#ifndef PARSER_H` způsob;
nepodporujeme staré compilery.

Všechny deklarace a prototypy by musí být v `.h` souborech a musí být logicky
seřazeny (např. všechny stack-related funkce by měly být u sebe).

  ```c
  // Project: Implementation of a compiler for the IFJ24 imperative language.
  // Author: John Fantomas (xfantom2d)
  //
  // Stuff for effective parsing of this and that and for working with
  // expression stacks.

  #pragma once

  #include "ast.h"


  typedef enum {
      OP_NEGATE = 0,
      OP_MULT= 1,
      OP_DIV = 1,
      OP_PLUS = 2,
      OP_MINUS = 2,
      OP_EQUAL = 3,
      OP_EQUAL_MORE = 3,
      OP_EQUAL_LESS = 3,
      OP_MORE = 3,
      OP_LESS = 3,
      OP_NOT_EQUAL = 3,
      OP_IS_NUL = 4
  } operator_priority;

  void expr_stack_init(expr_stack*);
  bool expr_stack_is_empty(const expr_stack*);
  bool expr_stack_is_full(const expr_stack*);
  ```

### 2. Naming Conventions

Pro konstanty a `enum` používejte `UPPER_SNAKE_CASE`.

Ve všech ostatních případech používejte `snake_case`. Vybírejte
deskriptivní jména, ale nebojte se je zkracovat. Například místo
`expression_stack_push` používejte `expr_stack_push`, nebo místo `binary_tree`
používejte `btree`.

`typedef` speciálně neodlišujte (nepoužívejte `_t`) a nechávejte je anonymní.
Tohle je validní.

  ```c
  typedef struct {
      expr_stack_node_type value;
      ast_node* next;
  } expr_node;
  ```

Hvězdička u definice pointeru je _vedle typu_, nikoliv vedle proměnné.
(správně: `expr_node* node`; špatně: `expr_node *node`). Dříve se hvězdičky
psaly u proměnných kvůli více deklaracím na jednom řádku. Například:

  ```c
  // `a` a `c` are pointing at `size_t`, whereas `b` _is_ `size_t`.
  size_t *a, b, *c;
  ```

U takovéhoto kódu by jiný typ rozmisťování hvězdiček nedával pořádný smysl. V
každém případě, viz [_variable declaration_](#7-variable-declaration) --
více deklarací na jednom řádků není povoleno.

### 3. Commenting Style

Pro single-line komentáře, používejte `//`.
Nemusíte je psát na vlastní řádek; pokud je napíšete vedle kódu,
odsaďte je dvěma mezerami od kódu (python style).

Pro multi-line, používejte blokové komentáře `/* */` v jakémkoliv formátu.
Hvězdičky seřaďte pod sebou do stejného sloupce.
Pro [dokumentaci funkcí](#4-documentation), přeskočte první a poslední řádek (na
kterém jsou respektive `/*` a `*/`).

Text uvnitř komentáře vždy odsaďtě aspoň jednou mezerou a dodržujte gramatická
pravidla (minimálně kapitalizace prvního písmena; věty zakončeny tečkou).
Všechny komentáře a dokumentaci piště __anglicky__.

  ```c
  // This is a valid single-line comment.
  uint32_t x = 0;  // Also valid: Next to code, two spaces before the comment.

  /* This is a valid
   * multi-line comment. */

  /* this is an invalid multi-line comment.
  * asterisks aren't aligned. sentences aren't capitalized. */
  ```

### 4. Documentation

Zdokumentujte _každou_ funkci. Používejte multi-line komentáře před signaturou
(implementace v `.c` souborech; dokumentaci nemusíte uvádět u prototypu v header
`.h` souborech), i v případech, kdy by se dokumentace vešla na jeden řádek.
První řádek multi-line bloku by měl začínat dvěma hvězdičkama (`/**`) a další
hvězdičky v komentáři by měly být seřazeny pod první hvězdičkou.

Uveďte:
 * krátký popis toho, pro co funkce slouží a co dělá
 * popis argumentů
 * popis return typu (mimo `void`, který je implicitní)
 * pokud nutno, popis předpokladů a invariant (např. "pointer nesmí být `NULL`",
   "string je case-sensitive",
   ["pointer nesmí být aliasovaný"](https://en.wikipedia.org/wiki/Restrict);
   invarianty jsou
   [popsany zde](https://softwareengineering.stackexchange.com/q/32727)).

Takovéto komentáře pište souvislým způsobem (nepoužívejte komentáře na styl
doxygen) a argumenty popisujte implicitně (nemusíte pro každý vytvářet vlastní
řádek). Argumenty uvádějte mezi tick apostrofy.

Předpoklady a invarianty lze také dokumentovat pomocí atributů
(například [`restrict`](https://en.wikipedia.org/wiki/Restrict),
[`[[nodiscard]]`](https://clang.llvm.org/docs/AttributeReference.html#nodiscard-warn-unused-result),
atd.), pokud vám nevadí extra podrobně zdokumentovaný kód. Berte ale na paměť,
že [tyto atributy jsou _assumed, but unchecked_](#11-validate-attributes).

Například:

  ```c
    /**
     * If `child` hasn't yet been assigned an ancestor, it is assigned to the
     * `ancestor` node. If `ancestor` doesn't have enough space for a new node,
     * it attempts to reallocate its children into a larger buffer.
     *
     * Returns `true` if the append succeeds, otherwise `false`.
     */
    [[nodiscard]] bool append_node(node const* restrict child,
                                   node const* restrict ancestor) {}
  ```

Zdokumentujte také konstanty, `struct` a `enum` a nejlépe i jejich elementy.
Některé názvy elementů jsou dostatečně sebe-dokumentující, ale nespoléhejte se
na to, že z názvu každý vyvodí, o co jde -- nebojte se být explicitní.
Elementy dokumentujte single-line komentama, i kdyby dokumentace zasahovala na
více řádků. Jestli pro každý koment uděláte vlastní řádek, nebo je napíšete
vedle kódu, je na vás. Tohle je validní dokumentace elementů:

  ```c
  typedef struct {
      expr_stack_node** stack;  // Buffer pre-allocated for the stack data.
      size_t capacity;          // The length of the `stack` buffer in elements.
      size_t top_idx;           // Index to the top element of the stack.
  } expr_stack;

  typedef struct {
      // Buffer pre-allocated for the inner stack data.
      expr_stack_node** stack;

      // The amount of elements the inner `stack` buffer is capable of holding.
      size_t capacity;

      // Index to the top element of the stack.
      size_t top_idx;
  } expr_stack;
  ```

Uvnitř kódu, __dokumentujte svůj úmysl; nebojte se být redundantní__.
Dokumentujte _co_ nějaký kód dělá, _proč_ nějaký kód něco dělá. Dokumentujte
proč se vyhýbáte určitým alternativám, proč se rozhodujete dělat něco "méně
efektivním způsobem" atd. atd. Zdokumentujte chybějící částí kódu a budoucí
optimalizace a implementace (`// TODO`), a handlování corner casů a chyb, o
kterých víte (`// XXX`).

### 5. Indentation, Spacing, Line Length

Pro odsazení používejte __4 mezery__, žádné taby.

Mezi operátory (`+`, `-`, `=`, atd.) pište mezery. Tohle se týká i komentářů.

Žádný trailing whitespace na konci řádků; nastavte si editory tak, aby vám je
automaticky promazávaly.

Délku řádků udržujte pod __80 znaků__.

### 6. Braces

Svorkujte podle [1TBS](https://en.wikipedia.org/wiki/Indentation_style#One_True_Brace).
Klidně nesvorkujte u single-line věcí, ale nemíchejte je s multi-line věcmi.

Tohle je v pohodě:

  ```c
  void expr_stack_init(expr_stack* stack) {
      stack->size = 0;
      stack->top = NULL;
  }

  if (condition)
      expr_stack_init(stack);
  else
      abort();
  ```

Tohle dělají čůráci:

  ```c
  if (condition)
      expr_stack_init(stack);
  else {
      printf("door stuck\n");
      abort();
  }
  ```

### 7. Variable Declaration

Deklarovat více proměnných na jednom řádku je zakázáno. Pokud je jakákoliv
šance, že někdo v týmu neví, co dělá tento kód (a někdo někde to určitě neví),
tak se jedná o špatný kód:

  ```c
  int* a, b, c;
  ```

Každou deklarovanou proměnnou ihned inicializujte
(podle [_safety pravidla_](#6-always-initialize-variables-and-prefer-calloc)).

Deklarujte své proměnné tam, kde se reálně využívají. V K&R verzi C (ještě
před ANSI C 89) se všechny proměnné musely deklarovat na začátku funkce. My
nepoužíváme C z roku 80.

Vyhněte se inicializaci proměnné a její kontrole na jednom řádku. Tohle je
špatný kód:

  ```c
  while ((line = fgets(buffer, sizeof(buffer), file)) != NULL) {}
  ```

## Safety, Correctness, Pitfall Prevention

### 1. Use `const` Extensively

Jako prevenci vůči nechtěným vedlejším efektům, když funkce nemodifikuje data,
explicitně deklarujte _pointer_ i _data_ na která odkazuje jako `const`.
* Pokud jsou pointer i data konstantní: `const uint32_t* const data;`
* Pokud jsou jenom data konstantní: `const uint32_t* data;`
* Pokud je jenom pointer konstantní, ale data se mění: `uint32_t* const data;`

### 2. Validate Input Arguments and Sizes

Ujistěte se, že pointery nejsou `NULL` a že odkazují na správnou paměť, a že
všechny velikosti a kapacity bufferů jsou validní pro dané buffery.

A vlastně vždycky validujte všechny invarianty.

### 3. Use Specific Types

Pro konzistenci mezi platformami a compilery a pro jasnější kód,
používejte `size_t` pro všechny proměnné, které reprezentují velikosti a indexy,
a specifické fixed-width typy ze `<stdint.h>` (`uint8_t`, `int32_t`, `uint64_t`,
atd.) místo generických typů jako `int`, `long` atd.

### 4. Avoid Unsafe Functions

Nepoužívejte zastaralé funkce jako `strcpy`, `sprintf`, `gets`, atd.

Kdokoliv, kdo nekontroluje bezpečnost funkcí, bude veřejně lynčován.

### 5. Be Explicit with Memory Ownership

Při jakékoliv práci s dynamickou pamětí ujasněte, kdo je vlastníkem paměti a kdo
je zodpovědný za její uvolnění.

Vždycky trackujte uvolněnou paměť. Nejjednodušší je nastavit pointer po uvolnění
na `NULL`, protože `free(NULL)` je `noop`, takže nemůže dojít k dvojitému
uvolnění atd. atd.

Stejně, _vždycky_ trackujte, kdo kde vlastní jakou paměť; pokud někdo drží
aliasovaný pointer a někdo jiný jej uvolní, to je budoucí segfault.

### 6. Always Initialize Variables and Prefer `calloc`

Vždycky inicializujte každou proměnnou, abyste se vyhnuli omylnému využívání
neinicializované paměti.

Pokud není po alokaci paměť ihned inicializována jiným způsobem, používejte
`calloc()`, který ji vynuluje.

### 7. Use Explicit Casting for Pointers

Nikdy nemanipulujte s `void` pointerama; vždycky je explicitně castněte na daný
typ.

### 8. Be Careful with Overflows

Ujistěte se, že všechny kalkulace jsou validní a že overflow není možný.
Napište extenzivní testy a vždycky zkoušejte, že vaše funkce fungují správně i s
extrémními hodnotami (např. `size_t !0`).

### 9. Avoid Non-Constant Globals

Vyhněte se nekonstantním globálním proměnným hodnotám. Jsou chaotické a nejsou
thread-safe.

### 10. Avoid Pointer Arithmetic

Pokud je to možné, používejte array indexování a `sizeof` místo pointer
aritmetiky.

### 11. Validate Attributes

Některé atributy (`restrict` a spol.) slouží jako rada, kterou může compiler
použít na lepší optimalizaci. Avšak tyhle atributy jsou _assumed, but unchecked_
-- compiler podle nich vygeneruje kód, ale pokud jsou dané předpoklady porušeny
(za což může programátor, nikoliv compiler), tak se jedná o undefined behavior.

#### `add(int* restrict a, int* restrict b, int n)`

[godbolt zde](https://godbolt.org/z/MWqP93c6Y).  
Bez použití `restrict` compiler vygeneruje kód pro explicitní kontrolu, zda-li
se jedná o překrývající se pointery.  
Pokud se nepřekrývají, použije `paddd` a pracuje na 8 `int`ech _najednou_.  
Pokud se překrývají, použije `add` a pracuje na 1 `int`u najednou
(i když je ten loop trošku optimalizovaný a jsou tam unrollnuté 4 akce na jeden
cyklus, takže vlastně pracuje na 4 `int`ech po sobě, nikoliv však najednou).

[godbolt zde](https://godbolt.org/z/WsM41T1Gv).  
S použítí `restrict` compiler rovnou vygeneruje vektorizovaný kód bez kontroly
překrývajících se pointerů. Vyvolat tuhle funkci s aliasovanými pointery je
undefined behavior, jelikož bylo compileru přislíbeno, že se tak nestane a že tak
může vektorizovat s jakýmikoliv argumenty.
