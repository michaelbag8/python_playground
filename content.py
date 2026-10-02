class Database:

    def __enter__(self):
        print("Connecting")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing")


with Database() as db:
    print("Querying")
