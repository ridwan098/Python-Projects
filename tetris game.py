  1 #======================================================================#
  2 # This file is part of YAT (Yet Another Tetris).                       #
  3 #                                                                      #
  4 # YAT is free software: you can redistribute it and/or modify          #
  5 # it under the terms of the GNU General Public License as published by #
  6 # the Free Software Foundation, either version 3 of the License, or    #
  7 # (at your option) any later version.                                  #
  8 #                                                                      #
  9 # YAT is distributed in the hope that it will be useful,               #
 10 # but WITHOUT ANY WARRANTY; without even the implied warranty of       #
 11 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the        #
 12 # GNU General Public License for more details.                         #
 13 #                                                                      #
 14 # You should have received a copy of the GNU General Public License    #
 15 # along with YAT.     If not, see <http://www.gnu.org/licenses/>.      #
 16 #======================================================================#
 17 
 18 #==========================================================================#
 19 # Name       : yat.py (Yet Another Tetris)                                 #
 20 # Description: Main game file for the tetris like game "yat"               #
 21 # Author     : Adrian Antonana                                             #
 22 # Date       : 17.08.2012                                                  #
 23 # Copyright  : Adrian Antonana 2012                                        #
 24 #==========================================================================#
 25 import pygame as pg
 26 import table  as tb
 27 import blocks as bk
 28 import colors as col
 29 
 30 #==========================================================================#
 31 #                     Global Variables and Constants                       #
 32 #==========================================================================#
 33 GAME_SPEED     = 500
 34 SPEED_INC_TICK = 50
 35 LINES_INC_TICK = 10
 36 LEVEL          = 1
 37 REMOVED_LINES  = 0
 38 MAX_LEVEL      = 10
 39 FPS            = 100
 40 
 41 #==========================================================================#
 42 #                           Function Definitions                           #
 43 #==========================================================================#
 44 
 45 #-------------------- Checks when blocks have to move down ----------------#
 46 def delay(ticks):
 47   return (ticks % GAME_SPEED) >= GAME_SPEED-10
 48 
 49 #------------------ Increases the Game Level and Game Speed ---------------#
 50 def incSpeed(remlines):
 51   global GAME_SPEED
 52   global LEVEL
 53 
 54   if LEVEL < MAX_LEVEL:
 55     if remlines / (LEVEL*LINES_INC_TICK) == 1:
 56       LEVEL += 1
 57       GAME_SPEED -= SPEED_INC_TICK
 58       return True
 59   return False
 60 
 61 #---------------------- Updates the information surface -------------------#
 62 def updateInfo(nb):
 63   global LEVEL_NUM_TEXT
 64   global LINES_NUM_TEXT
 65   global infosurface
 66 
 67   LEVEL_NUM_TEXT = font.render(str(LEVEL),True,col.WHITE)
 68   LINES_NUM_TEXT = font.render(str(REMOVED_LINES),True,col.WHITE)
 69   infosurface.fill(col.GREY_DARK)
 70   infosurface.blit(LEVEL_TEXT,LEVEL_TEXT_OFFSET)
 71   infosurface.blit(LEVEL_NUM_TEXT,LEVEL_NUM_TEXT_OFFSET)
 72   infosurface.blit(LINES_TEXT,LINES_TEXT_OFFSET)
 73   infosurface.blit(LINES_NUM_TEXT,LINES_NUM_TEXT_OFFSET)
 74   nb.show(infosurface,NEXT_BLOCK_OFFSET,20,INF_BLOCK_SIZE)
 75 
 76 
 77 #==========================================================================#
 78 #              Initialize pygame (display,mixer and clock)                 #
 79 #==========================================================================#
 80 pg.init()
 81 pg.mixer.init()
 82 sndblockplaced = pg.mixer.Sound("sounds/block_placed.wav")
 83 sndblockrotate = pg.mixer.Sound("sounds/block_rotate.wav")
 84 sndremovelines = pg.mixer.Sound("sounds/remove_lines.wav")
 85 sndlevelup     = pg.mixer.Sound("sounds/level_up.wav")
 86 sndgameover    = pg.mixer.Sound("sounds/game_over.wav")
 87 clock          = pg.time.Clock()
 88 pg.display.set_caption("yat - yet another tetris")
 89 pg.key.set_repeat(10,50)
 90 
 91 #==========================================================================#
 92 #                         Information surface                              #
 93 #==========================================================================#
 94 INFO_SURFACE_HEIGHT   = 105
 95 FONT_SIZE             = 30
 96 FONT_SIZE_GAME_OVER   = 60
 97 UPPER_OFFSET          = 20
 98 LEFT_OFFSET           = 10
 99 INF_BLOCK_SIZE        = 20
100 font                  = pg.font.SysFont(pg.font.get_default_font(),FONT_SIZE)
101 font_game_over        = pg.font.SysFont(pg.font.get_default_font(),
                            FONT_SIZE_GAME_OVER)
102 LEVEL_TEXT            = font.render("Level : ",True,col.WHITE)
103 LINES_TEXT            = font.render("Lines : ",True,col.WHITE)
104 LEVEL_TEXT_OFFSET     = (LEFT_OFFSET,UPPER_OFFSET)
105 LEVEL_NUM_TEXT_OFFSET = (70+LEFT_OFFSET,UPPER_OFFSET)
106 LINES_TEXT_OFFSET     = (LEFT_OFFSET,INFO_SURFACE_HEIGHT-40)
107 LINES_NUM_TEXT_OFFSET = (70+LEFT_OFFSET,INFO_SURFACE_HEIGHT-40)
108 NEXT_BLOCK_OFFSET     = tb.BLOCK_SIZE*tb.WIDTH - INF_BLOCK_SIZE * 5
109 
110 #==========================================================================#
111 #                            Game over text                                #
112 #==========================================================================#
113 GAME_OVER_TEXT        = font_game_over.render("GAME OVER",True,col.WHITE)
114 GAME_OVER_TEXT_OFFSET = ((tb.BLOCK_SIZE*tb.WIDTH/2)-120,(tb.BLOCK_SIZE*tb.
                            HEIGHT/2)-50)
115 
116 #==========================================================================#
117 #                         Initialize surfaces                              #
118 #==========================================================================#
119 screen         = pg.display.set_mode((tb.BLOCK_SIZE*tb.WIDTH,tb.
                     BLOCK_SIZE*tb.HEIGHT+INFO_SURFACE_HEIGHT))
120 tablesurface   = screen.subsurface((0,INFO_SURFACE_HEIGHT,tb.BLOCK_SIZE*tb.
                     WIDTH,tb.BLOCK_SIZE*tb.HEIGHT))
121 infosurface    = screen.subsurface((0,0,tb.BLOCK_SIZE*tb.WIDTH,
                     INFO_SURFACE_HEIGHT))
122 
123 #==========================================================================#
124 #                        Block spawn position                              #
125 #==========================================================================#
126 BLOCK_SPAWN_POS = (0,(tb.WIDTH/2)-1)
127 
128 #==========================================================================#
129 #               Create the table and an initial block                      #
130 #==========================================================================#
131 t     = tb.table(tablesurface)
132 b     = bk.block(BLOCK_SPAWN_POS)
133 nextb = bk.block(BLOCK_SPAWN_POS)
134 
135 #==========================================================================#
136 #                 Draw initial information surface                         #
137 #==========================================================================#
138 updateInfo(nextb)
139 
140 #==========================================================================#
141 #                            Main loop                                     #
142 #==========================================================================#
143 running = True
144 
145 while running:
146   clock.tick_busy_loop(FPS)
147   t.adBlock(b.getPosList(),b.getType())
148   t.show()
149 
150   # check if the fall delay has been reached. If yes, move block down.
151   if delay(pg.time.get_ticks()):
152     if b.canMovDown(t.getHeight(),t.getOcupPosList(b.getPosList())):
153       t.adBlock(b.getPosList(),bk.E)
154       b.movDown()
155     else:
156       # if the block can't move down, spawn a new block
157       t.adBlock(b.getPosList(),b.getType())
158       sndblockplaced.play()
159       retval = t.delFullLines()
160       if retval != 0:
161         sndremovelines.play()
162         REMOVED_LINES += retval
163         if incSpeed(REMOVED_LINES):
164           sndlevelup.play()
165       b.__init__(BLOCK_SPAWN_POS,nextb.getType())
166       nextb = bk.block(BLOCK_SPAWN_POS)
167       updateInfo(nextb)
168 
169       # check if the game is over
170       if t.gameOver(b.getPosList()):
171         t.adBlock(b.getPosList(),b.getType())
172         t.show()
173         running = False
174 
175   # get one event from the queue and perform action
176   event = pg.event.poll()
177   if event.type == pg.KEYDOWN:
178     key = event.key
179     if key == pg.K_ESCAPE:
180       running = False
181     elif key == pg.K_DOWN:
182       if b.canMovDown(t.getHeight(),t.getOcupPosList(b.getPosList())):
183         t.adBlock(b.getPosList(),bk.E)
184         b.movDown()
185       else:
186         # if the block can't move down, spawn a new block
187         t.adBlock(b.getPosList(),b.getType())
188         sndblockplaced.play()
189         retval = t.delFullLines()
190         if retval != 0:
191           sndremovelines.play()
192           REMOVED_LINES += retval
193           if incSpeed(REMOVED_LINES):
194             sndlevelup.play()
195         b.__init__(BLOCK_SPAWN_POS,nextb.getType())
196         nextb = bk.block(BLOCK_SPAWN_POS)
197         updateInfo(nextb)
198 
199         # check if the game is over
200         if t.gameOver(b.getPosList()):
201           t.adBlock(b.getPosList(),b.getType())
202           t.show()
203           running = False
204 
205     # move/rotate block left/right
206     elif key == pg.K_LEFT:
207       if b.canMovLeft(t.getWidth(),t.getOcupPosList(b.getPosList())):
208         t.adBlock(b.getPosList(),bk.E)
209         b.movLeft()
210     elif key == pg.K_RIGHT:
211       if b.canMovRight(t.getWidth(),t.getOcupPosList(b.getPosList())):
212         t.adBlock(b.getPosList(),bk.E)
213         b.movRight()
214     elif key == pg.K_LCTRL:
215       t.adBlock(b.getPosList(),bk.E)
216       if b.rotLeft(t.getHeight(),t.getWidth(),t.getOcupPosList(b.getPosList()
                       )):
217         sndblockrotate.play()
218     elif key == pg.K_LALT:
219       t.adBlock(b.getPosList(),bk.E)
220       if b.rotRight(t.getHeight(),t.getWidth(),t.getOcupPosList(b.getPosList(
                        ))):
221         sndblockrotate.play()
222 
223 #==========================================================================#
224 #                           The game is over                               #
225 #==========================================================================#
226 tablesurface.fill(col.BLACK)
227 t.setSurfAlpha(60)
228 t.show()
229 tablesurface.blit(GAME_OVER_TEXT,GAME_OVER_TEXT_OFFSET)
230 pg.display.flip()
231 sndgameover.play()
232 
233 quit = False
234 while not quit:
235   event = pg.event.wait()
236   if  event.type == pg.QUIT:
237     quit = True
238   if event.type == pg.KEYDOWN:
239     if event.key == pg.K_ESCAPE:
240       quit = True
