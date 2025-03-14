######################################################### -*- python -*-
# Cut and paste this line to import your macro after editing:
#
#     %run -i '/nsls2/data3/bmm/XAS/2024-1/313563/2024-03-21//wheel1_macro.py'
#
# Verify that your macro was loaded correctly:
#
#     wheel1_macro??
#
# Then run the macro:
#
#     RE(wheel1_macro())
#                /
############### / #######################################
#              / 
#             /  Note that you are defining a command
#            /   that gets run in BlueSky
#           V
from BMM.suspenders import BMM_suspenders, BMM_clear_suspenders
from BMM.functions import not_at_edge
def wheel1_macro(dryrun=False, ref=False):
    '''User-defined macro for running a sequence of XAFS measurements
    using a standard sample wheel
    '''
    (ok, text) = BMM_clear_to_start()
    if ok is False:
        print(error_msg('\n'+text) + bold_msg('Quitting macro....\n'))
        return(yield from null())

    BMMuser.macro_dryrun = dryrun
    BMMuser.prompt, BMMuser.running_macro = False, True
    BMMuser.instrument = 'double wheel'
    BMM_log_info('Beginning wheel1_macro')
    def main_plan(ref):

        ### ---------------------------------------------------------------------------------------
        ### BOILERPLATE ABOVE THIS LINE -----------------------------------------------------------
        ##  EDIT BELOW THIS LINE
        #<--indentation matters!

        ## change edge before starting, if needed...
        if not_at_edge('Mn', 'K'):
            yield from change_edge('Mn', edge='K', focus=False)

        report("Wheel sequence 1 of 5", level="bold", slack=True)
        yield from slot(3)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 205.00)
        yield from xafs('wheel1.ini', filename='Mn_Bixbyite', sample='Mn2O3', prep='PEG pellet')
        close_last_plot()

        report("Wheel sequence 2 of 5", level="bold", slack=True)
        yield from slot(4)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 205.00)
        yield from xafs('wheel1.ini', filename='Mn_Pyrolucite', sample='MnO2', prep='PEG pellet')
        close_last_plot()

        report("Wheel sequence 3 of 5", level="bold", slack=True)
        yield from slot(5)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 205.00)
        yield from xafs('wheel1.ini', filename='Mn_Rhodocrosite', sample='MnCO3', prep='PEG pellet')
        close_last_plot()

        report("Wheel sequence 4 of 5", level="bold", slack=True)
        yield from slot(9)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 40.00)
        yield from xafs('wheel1.ini', filename='Mn_Babingtonite', mode='both', sample='Ca2Fe0.75Mn0.25FeSi5O14(OH)', prep='PEG pellet', comment='Babingtonite, CM14452; Lane\'s Quarry, Westfield, Hampden County, Massachusetts', bounds='-200 -30 -10 25 560', times='1 1 1 1')
        close_last_plot()

        report("Wheel sequence 5 of 5", level="bold", slack=True)
        yield from xafs_wheel.outer() # outer ring
        yield from mv(xafs_det, 120.00)
        yield from change_edge('Fe', edge='K', focus=False)
        yield from xafs('wheel1.ini', filename='Fe_Babingtonite', mode='both', element='Fe', sample='Ca2Fe0.75Mn0.25FeSi5O14(OH)', prep='PEG pellet', comment='Babingtonite, CM14452; Lane\'s Quarry, Westfield, Hampden County, Massachusetts', bounds='-200 -30 -10 25 560', times='1 1 1 1')
        close_last_plot()

        if not dryrun:
            BMMuser.running_macro = False
            BMM_clear_suspenders()
            yield from shb.close_plan()


        ##  EDIT ABOVE THIS LINE
        ### BOILERPLATE BELOW THIS LINE -----------------------------------------------------------
        ### ---------------------------------------------------------------------------------------

    def cleanup_plan():
        yield from end_of_macro()
        yield from xafs_wheel.reset()
        (hours, minutes, seconds) = elapsed_time(start)
        report(f'{BMMuser.instrument} macro finished ({hours} hours, {minutes} minutes)', level='bold', slack=True)
        print(bold_msg('[Hint] to start Athena:\t\t') + '%athena')


    start = time.time()
    
    BMM_suspenders()
    yield from finalize_wrapper(main_plan(ref), cleanup_plan())    
    yield from end_of_macro()
    BMM_log_info('wheel1_macro finished!')
