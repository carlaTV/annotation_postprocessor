# Postprocessing texts annotated with Communicative Structure

Some codes to post-process the output of both manual and automatic annotations of Communicative Structure. For the moment, we stick to Thematicity.

The main usages of the codes will be the following:
* Check a list of errors in the output of the parser.
* Compute the accuracy of a parser or tagger.
* Compute the interannotator agreement.
* Tag with SSynt.

## Justification of the code

The __manual__ annotation of a text with Thematicity looks like this:

[It]T1 [even has the same amount of headline as all the other ones {[you]T1(P1.1) ['ve seen]R1(P1.1)}P1.1]R1 .

Each proposition is marked separately and numbered (following the scheme {}P1 {}P2). In old versions, embedded propositions were numbered independently to their parent propositions (e.g., {{}P2 {}P3}P1). Recently, we have decided to be consistent between the embedded and the parent propositions, following the scheme {}P1.1 {}P1.2}P1.

The tags for Thematicity are T (Theme), R (Rheme) and SP (Specifier). Embedded tags are remitted to the proposition they belong to: {[]SP(P2) []T(P2) []R(P2)}P2 

On the other hand, __automatic__ annotations don't include any annotation of propositions, but rather on the relation between thematicity spans. If the outer proposition has the following thematic division: []T []R, a parser would divide each span in the following way: [[]T(T)[]R(T)]T [[]SP(R)[]T(R)[]R(R)]R

The main aim of this code is to provide a common representation between __manual__ and __automatic__ annotations, and even between different annotators' outputs for them to be easily compared.
