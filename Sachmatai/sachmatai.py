# AI importai
import chess

# Lentos importai


################################################

# AI DALIS

################################################




# APSIRASOM KIEKVIENOS FIGUROS IVERTINIMA ESANT BETKOKIAME LENTOS LANGELYJE

pestininkoLenta = [
	0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

zirgoLenta = [
	-50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

rikioLenta = [
	-20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

bokstoLenta = [
	0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

valdovesLenta = [
	-20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]

karaliausLenta = [
	20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

# TIKRINAM AR ZAIDIMAS VIS DAR VYKSTA. JEIGU BAIGES - SURANDAM KAS LAIMEJO

if board.is_checkmate(): # jeigu sachas ir matas
	if board.turn:
		return -9999
	else:
		return 9999

if board.is_stalemate(): # jeigu lygiosios
	return 0

if board.is_insufficient_material(): # jeigu lygiosios, nes nebera figuru
	return 0

# SURANDAM KIEK BETKOKIU MEMENTU ANT LENTOS YRA FIGURU IR KOKIOS JOS
	# pirma raide - spalva, antra - figuros pavadinimas

bp = len(board.pieces(chess.PAWN, chess.WHITE))
jp = len(board.pieces(chess.PAWN, chess.BLACK))
bz = len(board.pieces(chess.KNIGHT, chess.WHITE))
jz = len(board.pieces(chess.KNIGHT, chess.BLACK))
br = len(board.pieces(chess.BISHOP, chess.WHITE))
jr = len(board.pieces(chess.BISHOP, chess.BLACK))
bb = len(board.pieces(chess.ROOK, chess.WHITE))
jb = len(board.pieces(chess.ROOK, chess.BLACK))
bv = len(board.pieces(chess.QUEEN, chess.WHITE))
jv = len(board.pieces(chess.QUEEN, chess.BLACK))

# SURANDAM BENDRA MATERIALA DAUGINANT SKIRTUMA TARP BALTU IR JUODU FIGURU KIEKIO IS TAM TIKROS FIGUROS VERTES
materialas = 100 * (bp - jp) + 320 * (bz - jz) + 330 * (br - jr) + 500 * (bb - jb) + 900 * (bv - jv)

# SURANDAM IS FIGURU LENTELIU KIEK FIGURA YRA VERTA TAM TIKRAME LANGELYJE IR PRIDEDAM KIEK TOKIU FIURU YRA
pestitinkuLangeliai = sum ([pestininkoLenta[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
pestitinkuLangeliai = pestitinkuLangeliai + sum ([-pestininkoLenta[chess.square_mirror(i)]
                                               for i in board.pieces(chess.PAWN, chess.BLACK)])

zirguLangeliai = sum ([zirgoLenta[i] for i in board.pieces (chess.KNIGHT, chess.WHITE)])
zirguLangeliai= zirguLangeliai + sum ([-zirgoLenta[chess.square_mirror(i)]
                           for i in board.pieces (chess.KNIGHT, chess.BLACK)])

rikiuLangeliai = sum([rikioLenta[i] for i in board.pieces (chess.BISHOP, chess.WHITE)])
rikiuLangeliai = rikiuLangeliai + sum ([-rikioLenta[chess.square_mirror(i)]
                           for i in board.pieces (chess.BISHOP, chess.BLACK)])

bokstuLangeliai = sum ([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
bokstuLangeliai = bokstuLangeliai + sum([-rookstable[chess.square_mirror(i)]
                       for i in board.pieces(chess.ROOK, chess.BLACK)])

valdoviuLangeliai = sum ([valdovesLenta[i] for i in board.pieces (chess.QUEEN, chess.WHITE)])
valdoviuLangeliai = valdoviuLangeliai + sum ([-valdovesLenta[chess.square_mirror(i)]
                         for i in board.pieces (chess.QUEEN, chess.BLACK)])

karaliuLangeliai = sum ([karaliausLenta[i] for i in board.pieces (chess.KING, chess.WHITE)])
karaliuLangeliai = karaliuLangeliai + sum ([-karaliausLenta[chess.square_mirror(i)]
                       for i in board.pieces (chess.KING, chess.BLACK)])

# SURANDAM BENDRA IVERTINIMA. + BALTIEMS, - JUODIEMS
ivertinimas = materialas + pestitinkuLangeliai + zirguLangeliai + rikiuLangeliai + bokstuLangeliai + valdoviuLangeliai + karaliuLangeliai

if board.turn:
    return ivertinimas
else:
    return -ivertinimas  
