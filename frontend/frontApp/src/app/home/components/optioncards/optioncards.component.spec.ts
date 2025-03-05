import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OptioncardsComponent } from './optioncards.component';

describe('OptioncardsComponent', () => {
  let component: OptioncardsComponent;
  let fixture: ComponentFixture<OptioncardsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OptioncardsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OptioncardsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
